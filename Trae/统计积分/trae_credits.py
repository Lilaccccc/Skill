#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
查询 Trae (CN) 积分消耗情况，支持自定义时间跨度。

用法示例：
    # 1) 用 "起始 ~ 结束" 一次性传入（推荐）
    python trae_credits.py "2026-10-01 00:00:00 ~ 2026-10-16 23:59:59"

    # 2) 分开传
    python trae_credits.py --start "2026-10-01 00:00:00" --end "2026-10-16 23:59:59"

    # 3) 指定 token
    python trae_credits.py "2026-10-01 00:00:00~2026-10-16 23:59:59" --token "<JWT>"

说明（经实测确认）：
    - 接口：POST {host}/trae/api/v1/pay/query_user_usage_group_by_session
      请求体：{start_time, end_time, page_size, page_num, usage_type}
        * start_time / end_time 为**秒**级时间戳（毫秒会返回 400）
        * page_size 必填，且不能超过 50（100 会返回 400）
        * usage_type 是**数组**，如 [1,2,3,4,5,6,7]；缺省或空数组会返回 total=0
          枚举：1=AutoCompletion 2=AdvancedModel 3=PremiumModelFastRequest
                4=PremiumModelSlowRequest 5=DollarBasic 6=DollarBonus 7=PayGo
      鉴权头：Authorization: Cloud-IDE-JWT <token>（注意是 Cloud-IDE-JWT，不是 Cloud-IDE-Token）
      响应：{total, user_usage_group_by_sessions:[{usage_time, credits_float, model_name,
             mode, session_id, extra_info:{input_token,output_token,...}}]}
    - token 获取顺序：--token > 环境变量 TRAE_TOKEN > 本地文件 ~/.trae-cn/trae-jwt-token
      （注意：~/.trae-cn/trae-jwt-token 通常是给沙箱工具用的临时 token，可能无权限，
       若报 401 请用 --token 传入一个有效 token）
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime

DEFAULT_HOST = "https://api.trae.cn"
DEFAULT_ENDPOINT = "/trae/api/v1/pay/query_user_usage_group_by_session"
TOKEN_FILE = os.path.join(os.path.expanduser("~"), ".trae-cn", "trae-jwt-token")
TIME_FMT = "%Y-%m-%d %H:%M:%S"
MAX_PAGE_SIZE = 50  # 服务端限制

USAGE_TYPE_NAMES = {
    "autocompletion": 1,
    "advancedmodel": 2,
    "premiummodelrequestfast": 3,
    "premiummodelfastrequest": 3,
    "premiummodelrequestslow": 4,
    "premiummodelslowrequest": 4,
    "dollarbasic": 5,
    "dollarbonus": 6,
    "paygo": 7,
}
ALL_USAGE_TYPES = [1, 2, 3, 4, 5, 6, 7]


def parse_range(value):
    """把 'start~end' 解析成 (start, end)。"""
    for sep in ("~", "～", " - ", " 至 "):
        if sep in value:
            left, right = value.split(sep, 1)
            return left.strip(), right.strip()
    return None, None


def parse_time(text):
    """支持 'yyyy-MM-dd HH:mm:ss'、'yyyy-MM-dd HH:mm'、'yyyy-MM-dd'。"""
    text = text.strip()
    for fmt in (TIME_FMT, "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    raise ValueError("无法解析时间：%r（应形如 2026-10-01 00:00:00）" % text)


def parse_usage_type(value):
    """把 'all' / '1,2' / 'AdvancedModel,PayGo' 解析成整数数组。"""
    if value is None:
        return list(ALL_USAGE_TYPES)
    value = value.strip()
    if not value or value.lower() == "all":
        return list(ALL_USAGE_TYPES)
    out = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if part.isdigit():
            out.append(int(part))
        else:
            key = part.replace("_", "").replace("-", "").lower()
            if key not in USAGE_TYPE_NAMES:
                raise ValueError("未知 usage_type：%r" % part)
            out.append(USAGE_TYPE_NAMES[key])
    return out or list(ALL_USAGE_TYPES)


def load_token(cli_token):
    if cli_token:
        return cli_token.strip()
    env = os.environ.get("TRAE_TOKEN")
    if env:
        return env.strip()
    if os.path.isfile(TOKEN_FILE):
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None


def to_epoch_seconds(dt):
    return int(time.mktime(dt.timetuple()))  # 本地时区


def call_api(host, token, payload):
    url = host.rstrip("/") + DEFAULT_ENDPOINT
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", "Cloud-IDE-JWT %s" % token)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        if e.code == 401:
            raise SystemExit(
                "接口返回 401 Unauthorized —— token 无效或已过期。\n"
                "请用 --token 传入有效 token（可登录 www.trae.cn 后从 DevTools 的 "
                "Network 里任一 /trae/api/ 请求复制 Authorization 头中的 JWT）。"
            )
        raise SystemExit("HTTP %s：%s" % (e.code, body[:300] or "(空响应体)"))
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        raise SystemExit("返回内容不是 JSON：\n%s" % body[:500])


def iter_records(resp):
    if not isinstance(resp, dict):
        return []
    node = resp.get("data", resp)
    if isinstance(node, dict):
        recs = node.get("user_usage_group_by_sessions")
        if isinstance(recs, list):
            return recs
    for key in ("user_usage_group_by_sessions", "list", "items"):
        if isinstance(resp.get(key), list):
            return resp[key]
    return []


def pick_credit(rec):
    for key in ("credits_float", "credits", "amount_float", "credit"):
        v = rec.get(key)
        if isinstance(v, (int, float)):
            return float(v)
    return 0.0


def fmt_time(rec):
    v = rec.get("usage_time")
    if isinstance(v, (int, float)) and v > 1_000_000_000:
        ts = v / 1000 if v > 10_000_000_000 else v
        return datetime.fromtimestamp(ts).strftime(TIME_FMT)
    return "-"


def main():
    ap = argparse.ArgumentParser(description="查询 Trae 积分消耗（支持自定义时间跨度）")
    ap.add_argument("range", nargs="?", help='"起始 ~ 结束"，如 "2026-10-01 00:00:00 ~ 2026-10-16 23:59:59"')
    ap.add_argument("--start", help="起始时间 yyyy-MM-dd HH:mm:ss")
    ap.add_argument("--end", help="结束时间 yyyy-MM-dd HH:mm:ss")
    ap.add_argument("--token", help="Cloud-IDE-JWT；缺省读环境变量 TRAE_TOKEN 或 ~/.trae-cn/trae-jwt-token")
    ap.add_argument("--host", default=DEFAULT_HOST, help="接口域名，默认 %s" % DEFAULT_HOST)
    ap.add_argument("--usage-type", default=None,
                    help="usage_type，缺省为全部：all 或用逗号分隔（如 2,3 或 AdvancedModel,PayGo）")
    ap.add_argument("--page-size", type=int, default=MAX_PAGE_SIZE, help="每页条数，最大 %d" % MAX_PAGE_SIZE)
    ap.add_argument("--max-pages", type=int, default=500, help="最多翻页数，防死循环")
    ap.add_argument("--raw", action="store_true", help="打印原始响应（调试用）")
    args = ap.parse_args()

    start_s, end_s = (args.start, args.end)
    if args.range:
        rs, re_ = parse_range(args.range)
        if rs and re_:
            start_s, end_s = rs, re_
    if not start_s or not end_s:
        ap.error('需要时间跨度，例如：trae_credits.py "2026-10-01 00:00:00 ~ 2026-10-16 23:59:59"')

    try:
        start_dt, end_dt = parse_time(start_s), parse_time(end_s)
        usage_types = parse_usage_type(args.usage_type)
    except ValueError as e:
        raise SystemExit(str(e))
    if end_dt < start_dt:
        raise SystemExit("结束时间早于起始时间")

    page_size = min(max(1, args.page_size), MAX_PAGE_SIZE)

    token = load_token(args.token)
    if not token:
        raise SystemExit("未找到 token：请用 --token 传入，或设置 TRAE_TOKEN 环境变量。")

    print("查询区间：%s ~ %s" % (start_dt, end_dt))
    print("usage_type：%s  page_size：%d" % (usage_types, page_size))
    print("-" * 78)

    base = {
        "start_time": to_epoch_seconds(start_dt),
        "end_time": to_epoch_seconds(end_dt),
        "page_size": page_size,
        "usage_type": usage_types,
    }

    total_credits = 0.0
    rows = []
    total_expected = None
    for page in range(1, args.max_pages + 1):
        payload = dict(base, page_num=page)
        resp = call_api(args.host, token, payload)
        if args.raw:
            print(json.dumps(resp, ensure_ascii=False, indent=2))
        if total_expected is None:
            total_expected = resp.get("total") if isinstance(resp, dict) else None
        recs = iter_records(resp)
        if not recs:
            break
        for rec in recs:
            c = pick_credit(rec)
            total_credits += c
            rows.append((
                fmt_time(rec),
                c,
                str(rec.get("model_name") or "-"),
                str(rec.get("mode") or "-"),
                str(rec.get("session_id") or "-"),
            ))
        if len(recs) < page_size:
            break
        if total_expected is not None and len(rows) >= total_expected:
            break

    if not rows:
        print("该区间内没有返回消耗记录。")
        return

    rows.sort(key=lambda r: r[0])
    wt = max(len(r[0]) for r in rows)
    wm = max(len(r[2]) for r in rows)
    print("%-*s  %10s  %-*s  %-5s  %s" % (wt, "时间", "积分", wm, "模型", "模式", "会话"))
    for t, c, m, mode, sid in rows:
        print("%-*s  %10.4f  %-*s  %-5s  %s" % (wt, t, c, wm, m, mode, sid))
    print("-" * 78)
    print("记录数：%d%s，积分消耗合计：%.4f" % (
        len(rows),
        ("（服务端 total=%s）" % total_expected) if total_expected is not None else "",
        total_credits,
    ))


if __name__ == "__main__":
    main()
