---
name: natural-organic-style
description: Natural Organic（自然有机风）UI 设计系统 Skill。当用户要求生成自然有机风、温暖大地色系（amber/stone/olive/sage）、米色背景、有机 blob 圆角的网页/组件/着陆页，或明确提到 "Natural Organic"、"自然有机风"、style_slug natural-organic 时使用。提供精确 Token 字典、组件骨架模板、禁止项清单与交付前自检流程，防止风格漂移。
---

# Natural Organic（自然有机风）Style Skill

温暖自然的有机风格：大地色系、米色纸张质感背景、有机 blob 形状、衬线标题。适合健康品牌、有机食品、环保产品、手工艺品网站。

## 什么时候使用

- 用户要求生成「自然有机风 / Natural Organic」风格的页面或组件
- 用户要求按 style_slug `natural-organic` 生成代码
- 用户给出健康/有机/环保/手工类产品需求且指定温暖自然风格

## 工作流程

1. **读取完整风格规范**：先读取 `references/style-reference.md`，获取完整 Token 字典、禁止项、组件骨架模板和自检清单。不要凭记忆套用规则。
2. **套用 Token 生成代码**：严格使用规范中的 class token 映射（按钮、卡片、输入框等必须项逐字使用）。
3. **交付前自检**：对照 style-reference.md 末尾的「生成后自检清单」逐项确认，任何一项不通过就修改后再交付。

## 必须遵守（最高优先级摘要）

- 大地色系：amber / stone / olive / sage；背景 `bg-[#faf6f1]`、`bg-amber-50`
- 有机圆角：`rounded-[2rem]` 或 blob 形状；禁止尖锐几何形与完美矩形
- 标题 `font-serif`，正文 `font-sans text-stone-600`
- 动画：duration-500+、ease-in-out，支持 prefers-reduced-motion
- 禁止：冷色调（蓝/紫）、纯黑 `#000000`、霓虹/高饱和色、渐变 `bg-gradient-to-*`、`shadow-lg/xl/2xl` 等

## 禁止项（匹配即拒绝，直接重写）

完整禁止 class 与模式列表见 `references/style-reference.md` 的 [FORBIDDEN] 章节。出现即视为风格违规，不找借口重写。

## 详细规范

所有 Token、模板、示例 Prompt、自检清单见：

- `references/style-reference.md` —— 完整 Natural Organic 风格规范
