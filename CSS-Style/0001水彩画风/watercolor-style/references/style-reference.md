# Watercolor Style Reference（完整风格规范）

> 本文件由 `watercolor-style` Skill 引用。生成代码前必须完整阅读；规则冲突时，以「绝对禁止」为最高优先级。

## 1. 核心理念

水彩画风模拟颜料在湿纸上自然渗透：颜色半透明、边缘模糊、层次由叠色产生。

- **流动感**：颜色像水彩一样自然渗透、扩散
- **柔和边缘**：没有硬朗边界，一切都柔和过渡
- **纸张质感**：底层保留水彩纸的温暖与细微颗粒
- **透明叠加**：颜色以低透明度层层叠加，而不是大块实色

**适合**：品牌站、作品集、画廊、博客、个人主页、活动/婚礼页面、登录与联系表单。

**不适合**：高密度后台表格、强对比操作的仪表盘。这类界面最多借用纸色与圆角，不要铺满晕染色块。

---

## 2. 执行要求

- 优先保证风格一致性，再做创意延展。
- 遇到冲突时，以「绝对禁止」为最高优先级。
- 只使用第 3 节的水彩调色板，不引入第二套近似色。
- 输出前自检：颜色、排版、间距、交互是否仍属于水彩画风。

---

## 3. 配色

### 3.1 基础色

| 角色 | 色值 | Tailwind 用法 |
| --- | --- | --- |
| 纸张主背景 | `#faf8f5` | `bg-[#faf8f5]` |
| 纸张辅背景（导航/页脚/表单区） | `#f0ebe3` | `bg-[#f0ebe3]` |
| 正文主色 | `#3a3a3a` | `text-[#3a3a3a]` |
| 主色（链接/标题/主按钮） | `#4a6fa5` | `text-[#4a6fa5]` `bg-[#4a6fa5]` |
| 深主色（浅彩底上的小字） | `#3f628f` | `text-[#3f628f]` |
| 弱化正文（仅纸色底） | `#6f6a63` | `text-[#6f6a63]` |
| 装饰弱化（仅大字号/装饰） | `#8a8a8a` | `text-[#8a8a8a]` |

### 3.2 水彩四色

| 名称 | 色值 | 典型用法 |
| --- | --- | --- |
| 蜜桃 Peach | `#e8a87c` | 暖色晕染、同色系悬停阴影 |
| 青绿 Teal | `#85cdca` | 冷色晕染、与蜜桃对置 |
| 玫瑰 Rose | `#c38d94` | 强调色、引文底色 |
| 沙色 Sand | `#d4a373` | 中性暖色、辅助晕染 |

### 3.3 使用配比

- 纸张色与辅纸色占画面 80–90%。
- 同一屏主水彩不超过 2–3 种，透明度控制在 `/10`–`/30`。
- 蓝灰 `#4a6fa5` 只用于文字、按钮、细边框和小面积色块，不做大面积实色背景。
- 不使用霓虹色、荧光色、高饱和纯色。

### 3.4 对比度约束（WCAG 2.1 AA）

- 正文与交互文字 ≥ 4.5:1；大字（≥24px）≥ 3:1。本风格禁用粗体，因此所有小字都按 4.5:1 要求。
- **可用组合**：
  - `#3a3a3a` 放在 `#faf8f5`、`#f0ebe3` 或浅水彩底上
  - `#6f6a63` 放在 `#faf8f5` 上（约 5.1:1）
  - `#4a6fa5` 放在 `#faf8f5` 上（约 4.9:1）
  - `#3f628f` 放在 `#f0ebe3` 或浅水彩底上（约 5.3:1）
  - `text-white` 放在 `bg-[#4a6fa5]` 上（约 4.9:1）
- **禁用组合**：
  - `#8a8a8a` 用作正文或小字（约 3.3:1，仅可用于装饰/大字）
  - `#6f6a63` 放在彩色晕染底上（会跌破 4.5:1）
  - `text-white` 放在 `bg-[#4a6fa5]/80` 上（约 3.5:1，不合规）
  - 灰色文字放在彩色背景上

### 3.5 按钮配色

- 主按钮：`bg-[#4a6fa5] text-white`；悬停不改变填充透明度，用彩色阴影晕开。
- 次按钮：`bg-[#faf8f5] text-[#4a6fa5] border border-[#4a6fa5]/30`。
- 文字按钮：`text-[#4a6fa5]`，悬停用下划线或轻微阴影，不做背景填充。

---

## 4. 字体与排版

### 4.1 字体族

- 标题：`font-serif font-light tracking-wide`
- Hero 标题、引文可加 `italic`；中文斜体效果生硬时只保留衬线
- 正文：`font-sans font-light leading-relaxed`
- 等宽：`font-mono`
- 禁止 Inter / Roboto / Geist 等过度使用的字体
- 推荐衬线：Cormorant Garamond、EB Garamond、Noto Serif SC、思源宋体
- 推荐正文：Noto Sans SC、思源黑体、PingFang SC、系统无衬线字体

```css
/* Tailwind v4；v3 请写入 tailwind.config 的 theme.extend.fontFamily */
@theme {
  --font-serif: "Cormorant Garamond", "Noto Serif SC", "Songti SC", Georgia, serif;
  --font-sans: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", system-ui, sans-serif;
}
```

### 4.2 字重

只用 `font-light` 与常规字重。禁止 `font-black`、`font-bold`、`font-semibold`、`font-extrabold`；层次用字号、字距、颜色和留白建立。

### 4.3 字号

| 层级 | Class |
| --- | --- |
| Hero | `text-3xl md:text-5xl lg:text-6xl` |
| H1 | `text-2xl md:text-4xl` |
| H2 | `text-xl md:text-3xl` |
| H3 | `text-lg md:text-xl` |
| 正文 | `text-sm md:text-base` |
| 小字 | `text-xs md:text-sm` |

### 4.4 排版规则

- 正文行宽 `max-w-[65ch]` 到 `max-w-[72ch]`，不要超过 75 个字符。
- 标题与正文之间用 1–1.5 倍行距的留白过渡，不靠粗体压层级。
- 小标签使用正常大小写（`text-xs md:text-sm`），禁止 tiny uppercase tracked eyebrow（如 `text-[10px] uppercase tracking-[0.3em]`）。

---

## 5. Token 字典

### 5.1 边框与圆角

```
常规边框: border border-[#4a6fa5]/20
强调边框（少用）: border-[#4a6fa5]/30
按钮/输入框: rounded-2xl
卡片: rounded-2xl md:rounded-3xl
色块/胶囊: rounded-full
```

禁止：`rounded-none`、`rounded-sm`、`rounded-md`、`rounded-lg`、`border-2`、`border-4`、`border-black`。

### 5.2 阴影

```
小:   shadow-[0_2px_10px_rgba(74,111,165,0.1)]
中:   shadow-[0_4px_20px_rgba(74,111,165,0.12)]
大:   shadow-[0_8px_30px_rgba(74,111,165,0.15)]
聚焦: shadow-[0_4px_20px_rgba(74,111,165,0.15)]
晕开: hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)]
按压: active:shadow-[inset_0_2px_10px_rgba(74,111,165,0.2)]
```

同色系悬停阴影（按元素主色选择）：

| 主色 | 悬停阴影 |
| --- | --- |
| 蓝灰 | `hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)]` |
| 蜜桃 | `hover:shadow-[0_10px_40px_rgba(232,168,124,0.35)]` |
| 青绿 | `hover:shadow-[0_10px_40px_rgba(133,205,202,0.35)]` |
| 玫瑰 | `hover:shadow-[0_10px_40px_rgba(195,141,148,0.35)]` |
| 沙色 | `hover:shadow-[0_10px_40px_rgba(212,163,115,0.35)]` |

### 5.3 动效

```
过渡:     transition-all duration-500 ease-in-out
悬停缩放: hover:scale-[1.02]（按钮）；hover:scale-[1.01]（卡片，可选）
悬停位移: 禁止 translate-y 上浮
按压:     active:scale-[0.98] + 内阴影
聚焦:     focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5]
减弱动效: motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:active:scale-100
```

禁止 `duration-75/100/150/200/300/400` 等低于 500ms 的交互过渡；禁止 `ease-linear`、`ease-in`、`ease-out`、bounce、elastic 缓动，交互统一 `ease-in-out`。

### 5.4 间距

```
Section: py-12 md:py-20 lg:py-28
容器:   px-4 md:px-8 lg:px-12
卡片:   p-5 md:p-8
小间距: gap-3 md:gap-4
中间距: gap-4 md:gap-6
大间距: gap-6 md:gap-10
```

### 5.5 颜色角色

```
背景主色: bg-[#faf8f5]
背景辅色: bg-[#f0ebe3]
背景晕染色: bg-[#4a6fa5]/10, bg-[#e8a87c]/15, bg-[#85cdca]/15, bg-[#c38d94]/12, bg-[#d4a373]/15
正文主色: text-[#3a3a3a]
正文辅色: text-[#4a6fa5]
浅彩底小字: text-[#3f628f]
正文弱化色: text-[#6f6a63]（仅纸色底）
按钮主色: bg-[#4a6fa5] text-white
按钮辅色: bg-[#faf8f5] text-[#4a6fa5] border border-[#4a6fa5]/30
```

---

## 6. 水彩特效配方

### 6.1 纸张底

页面底色必须是 `bg-[#faf8f5]`，区块之间可用 `bg-[#f0ebe3]` 区分。不要用纯白铺满整页。

可选纸张颗粒（低透明度，不能影响文字对比度）：

```css
.paper-grain {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 200px 200px;
  opacity: 0.035;
  mix-blend-mode: multiply;
  pointer-events: none;
}
```

### 6.2 多层径向晕染

用多个 `radial-gradient` 叠出颜料渗透感，单层必须柔和收尾：

```html
<div aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_18%_22%,rgba(232,168,124,0.35),transparent_58%),radial-gradient(circle_at_82%_28%,rgba(133,205,202,0.28),transparent_55%),radial-gradient(circle_at_50%_92%,rgba(195,141,148,0.22),transparent_60%)]"></div>
```

### 6.3 blur 色块扩散

大面积晕染用独立色块 + `blur-3xl`，必须 `aria-hidden`、`pointer-events-none`，父级 `relative overflow-hidden`：

```html
<div aria-hidden="true" class="pointer-events-none absolute inset-0">
  <div class="absolute -left-24 -top-20 h-80 w-80 rounded-full bg-[#e8a87c]/30 blur-3xl"></div>
  <div class="absolute -right-24 top-1/4 h-96 w-96 rounded-full bg-[#85cdca]/30 blur-3xl"></div>
  <div class="absolute -bottom-28 left-1/3 h-80 w-80 rounded-full bg-[#c38d94]/25 blur-3xl"></div>
</div>
```

### 6.4 卡片湿纸渐变

卡片底色先写 `bg-[#faf8f5]`，再叠一层低透明度渐变（背景色与背景图可共存）：

```
bg-[#faf8f5] bg-gradient-to-br from-[#e8a87c]/20 via-[#faf8f5] to-[#85cdca]/20
hover:from-[#e8a87c]/30 hover:to-[#85cdca]/30
```

如果需要真正平滑的湿纸过渡（渐变停靠点在部分浏览器不会逐帧插值），用同色 overlay + 透明度过渡。父级需 `group relative`，overlay 放在内容之前，内容层加 `relative`：

```html
<div aria-hidden="true" class="pointer-events-none absolute inset-0 bg-gradient-to-br from-[#e8a87c]/20 to-[#85cdca]/20 opacity-60 transition-opacity duration-500 ease-in-out group-hover:opacity-100"></div>
```

### 6.5 柔和边缘

所有容器用 `rounded-2xl` / `md:rounded-3xl`，配 `border border-[#4a6fa5]/20` 与低透明度阴影。边框只做 1px 细线，不做色块描边或单侧粗线。

---

## 7. 动效与交互规则

### 7.1 颜料晕开（Pigment Bloom）

悬停不要 `translate-y` / `-translate-y`。让同色系彩色阴影大幅向外扩散：

```html
hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)]
```

### 7.2 湿纸效果（Damp Paper）

悬停时让渐变底色略微加深，模拟纸张吸水：

```html
from-[#e8a87c]/20 hover:from-[#e8a87c]/30
```

### 7.3 液态缓动（Liquid Slowness）

所有交互统一 `transition-all duration-500 ease-in-out`。禁止低于 500ms、`ease-linear`、bounce/elastic 曲线。

### 7.4 柔和按压（Soft Press）

按压用 `active:scale-[0.98]` + 内阴影：

```html
active:scale-[0.98] active:shadow-[inset_0_2px_10px_rgba(74,111,165,0.2)]
```

### 7.5 焦点与减弱动效

- 所有可交互元素必须有可见焦点：`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5]`。
- 所有动效提供 reduced-motion 备选：`motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:active:scale-100`。

---

## 8. 绝对禁止（匹配即拒绝）

### 8.1 禁止的 Class

- `rounded-none`
- `rounded-sm`
- `rounded-md`
- `rounded-lg`
- `border-black`
- `border-2`
- `border-4`
- `border-l-4` / `border-r-4`（单侧粗边框装饰）
- `shadow-[2px_2px_0px...]`
- `shadow-[4px_4px_0px...]`
- `shadow-[8px_8px_0px...]`
- `font-black`
- `font-bold`
- `font-semibold`
- `font-extrabold`
- `bg-black`
- `bg-[#1a1a1a]`
- `text-black`
- `duration-75` / `duration-100` / `duration-150` / `duration-200` / `duration-300` / `duration-400`
- `ease-linear`
- `ease-in`
- `ease-out`

### 8.2 禁止的模式

- 匹配 `^rounded-(?:none|sm|md|lg)$`
- 匹配 `^shadow-\[\d+px_\d+px_0px`
- 匹配 `^border-(?:black|2|4)$`
- 匹配 `^font-(?:black|bold|semibold|extrabold)$`
- 匹配 `^bg-(?:black|\[#1a1a)`
- 匹配 `^ease-(?:linear|in|out)$`
- 紫色到蓝色的渐变
- 渐变文字（`bg-clip-text text-transparent`）
- 玻璃态作为默认风格（不做全站 backdrop-blur 卡片；导航可轻微半透明）
- 嵌套卡片（卡片里再放卡片）
- 彩色背景上的灰色小字
- 每个 section 标题上方的 tiny uppercase tracked eyebrow
- 纯黑背景、硬边框、直角、过度饱和/刺眼的颜色

### 8.3 禁止原因

- `rounded-none/sm/md/lg`：水彩风只用大圆角（`rounded-2xl` 到 `rounded-3xl`）
- `border-2/4`：水彩风只用 1px 细边框，粗边框会破坏纸面感
- 硬偏移阴影：水彩风用柔和扩散阴影，不用硬边贴纸阴影
- `font-bold` 及更重字重：水彩风用 light/regular 呈现轻盈感
- 快速缓动：颜料扩散是缓慢的，快速切换会显得机械

---

## 9. 必须包含

### 9.1 按钮必须包含

```
rounded-2xl
shadow-[0_4px_20px_rgba(74,111,165,0.12)]
hover:scale-[1.02]
hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)]
active:scale-[0.98]
active:shadow-[inset_0_2px_10px_rgba(74,111,165,0.2)]
transition-all
duration-500
ease-in-out
font-light
focus-visible:ring-2
```

### 9.2 卡片必须包含

```
rounded-2xl
md:rounded-3xl
border
border-[#4a6fa5]/20
shadow-[0_4px_20px_rgba(74,111,165,0.12)]
bg-[#faf8f5]
p-5 md:p-8
transition-all duration-500 ease-in-out
```

带湿纸效果的卡片另加 `bg-gradient-to-br from-[#e8a87c]/20 via-[#faf8f5] to-[#85cdca]/20` 与 `hover:from-[#e8a87c]/30 hover:to-[#85cdca]/30`。

### 9.3 输入框必须包含

```
rounded-2xl
border
border-[#4a6fa5]/20
bg-white/60
font-light
focus:shadow-[0_4px_20px_rgba(74,111,165,0.15)]
focus:outline-none
focus-visible:ring-2
```

---

## 10. 错误 vs 正确对比

以下错误示例只代表「未经过当前风格适配的通用默认值」，不要当作视觉建议。

### 10.1 按钮

[WRONG] 通用组件库默认样式：

```html
<button class="{GENERIC_LIBRARY_BUTTON_DEFAULT}">点击我</button>
```

[CORRECT] 水彩风按钮 token：

```html
<button class="inline-flex items-center justify-center rounded-2xl px-6 py-3 shadow-[0_4px_20px_rgba(74,111,165,0.12)] hover:scale-[1.02] hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)] active:scale-[0.98] active:shadow-[inset_0_2px_10px_rgba(74,111,165,0.2)] transition-all duration-500 ease-in-out font-light bg-[#4a6fa5] text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:active:scale-100">
  点击我
</button>
```

### 10.2 卡片

[WRONG] 未经风格适配的通用卡片：

```html
<div class="{GENERIC_LIBRARY_CARD_DEFAULT}">
  <h3>{TITLE}</h3>
</div>
```

[CORRECT] 水彩风卡片 token：

```html
<article class="rounded-2xl md:rounded-3xl border border-[#4a6fa5]/20 bg-[#faf8f5] bg-gradient-to-br from-[#e8a87c]/20 via-[#faf8f5] to-[#85cdca]/20 p-5 md:p-8 shadow-[0_4px_20px_rgba(74,111,165,0.12)] transition-all duration-500 ease-in-out hover:from-[#e8a87c]/30 hover:to-[#85cdca]/30 hover:shadow-[0_10px_40px_rgba(232,168,124,0.30)]">
  <h3 class="font-serif font-light tracking-wide text-[#4a6fa5] text-lg md:text-xl">{TITLE}</h3>
  <p class="mt-3 font-sans font-light text-[#3a3a3a] text-sm md:text-base leading-relaxed">{DESCRIPTION}</p>
</article>
```

### 10.3 输入框

[WRONG] 未经风格适配的通用输入框：

```html
<input class="{GENERIC_LIBRARY_INPUT_DEFAULT}" />
```

[CORRECT] 水彩风输入框 token：

```html
<input class="w-full rounded-2xl border border-[#4a6fa5]/20 bg-white/60 px-4 py-3 text-[#3a3a3a] placeholder:text-[#6f6a63] font-light shadow-[0_2px_10px_rgba(74,111,165,0.1)] focus:outline-none focus:shadow-[0_4px_20px_rgba(74,111,165,0.15)] focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5] transition-all duration-500 ease-in-out" placeholder="{PLACEHOLDER}" />
```

---

## 11. 页面骨架模板

以下骨架只使用当前风格的 token。替换 `{PLACEHOLDER}` 时，不要移除或替换这些 token。

### 11.1 导航栏

```html
<nav class="sticky top-0 z-40 bg-[#faf8f5]/90 text-[#3a3a3a] border-b border-[#4a6fa5]/20 px-4 md:px-8 lg:px-12">
  <div class="flex items-center justify-between max-w-6xl mx-auto gap-3 md:gap-4 min-h-16">
    <a href="/" class="font-serif font-light tracking-wide text-[#4a6fa5] text-lg md:text-xl">
      {LOGO_TEXT}
    </a>
    <div class="flex items-center gap-4 md:gap-6 font-sans font-light text-xs md:text-sm">
      <!-- 每个导航项重复此结构 -->
      <a href="#" class="transition-colors duration-500 ease-in-out hover:text-[#4a6fa5]">{NAV_LINK_TEXT}</a>
    </div>
  </div>
</nav>
```

### 11.2 Hero 区块

```html
<section class="relative overflow-hidden bg-[#faf8f5] text-[#3a3a3a] py-12 md:py-20 lg:py-28 px-4 md:px-8 lg:px-12">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0">
    <div class="absolute -left-24 -top-20 h-80 w-80 rounded-full bg-[#e8a87c]/30 blur-3xl"></div>
    <div class="absolute -right-24 top-1/4 h-96 w-96 rounded-full bg-[#85cdca]/30 blur-3xl"></div>
    <div class="absolute -bottom-28 left-1/3 h-80 w-80 rounded-full bg-[#c38d94]/25 blur-3xl"></div>
  </div>
  <div class="relative max-w-4xl mx-auto">
    <h1 class="font-serif font-light italic tracking-wide text-[#4a6fa5] text-3xl md:text-5xl lg:text-6xl">
      {HEADLINE}
    </h1>
    <p class="mt-4 md:mt-6 font-sans font-light leading-relaxed max-w-[65ch] text-sm md:text-base">
      {SUBHEADLINE}
    </p>
    <button class="mt-6 md:mt-8 inline-flex items-center justify-center rounded-2xl px-6 py-3 shadow-[0_4px_20px_rgba(74,111,165,0.12)] hover:scale-[1.02] hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)] active:scale-[0.98] active:shadow-[inset_0_2px_10px_rgba(74,111,165,0.2)] transition-all duration-500 ease-in-out font-light bg-[#4a6fa5] text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:active:scale-100">
      {CTA_TEXT}
    </button>
  </div>
</section>
```

### 11.3 卡片网格

```html
<section class="bg-[#faf8f5] text-[#3a3a3a] py-12 md:py-20 lg:py-28 px-4 md:px-8 lg:px-12">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-serif font-light tracking-wide text-[#4a6fa5] text-xl md:text-3xl">{SECTION_TITLE}</h2>
    <div class="mt-6 md:mt-10 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
      <!-- 每张卡片轮换一种水彩主色；不要嵌套卡片 -->
      <article class="rounded-2xl md:rounded-3xl border border-[#4a6fa5]/20 bg-[#faf8f5] bg-gradient-to-br from-[#e8a87c]/20 via-[#faf8f5] to-[#85cdca]/20 p-5 md:p-8 shadow-[0_4px_20px_rgba(74,111,165,0.12)] transition-all duration-500 ease-in-out hover:from-[#e8a87c]/30 hover:to-[#85cdca]/30 hover:shadow-[0_10px_40px_rgba(232,168,124,0.30)]">
        <h3 class="font-serif font-light tracking-wide text-[#4a6fa5] text-lg md:text-xl">{CARD_TITLE}</h3>
        <p class="mt-3 font-sans font-light text-[#3a3a3a] text-sm md:text-base leading-relaxed">{CARD_DESCRIPTION}</p>
      </article>
    </div>
  </div>
</section>
```

### 11.4 表单

```html
<section class="bg-[#f0ebe3] py-12 md:py-20 lg:py-28 px-4 md:px-8 lg:px-12">
  <div class="max-w-2xl mx-auto rounded-2xl md:rounded-3xl border border-[#4a6fa5]/20 bg-[#faf8f5] p-5 md:p-8 shadow-[0_4px_20px_rgba(74,111,165,0.12)]">
    <h2 class="font-serif font-light tracking-wide text-[#4a6fa5] text-xl md:text-3xl">{FORM_TITLE}</h2>
    <form class="mt-6 md:mt-8 space-y-4 md:space-y-6">
      <label class="block">
        <span class="font-sans font-light text-[#3a3a3a] text-sm md:text-base">{LABEL}</span>
        <input class="mt-2 w-full rounded-2xl border border-[#4a6fa5]/20 bg-white/60 px-4 py-3 text-[#3a3a3a] placeholder:text-[#6f6a63] font-light shadow-[0_2px_10px_rgba(74,111,165,0.1)] focus:outline-none focus:shadow-[0_4px_20px_rgba(74,111,165,0.15)] focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5] transition-all duration-500 ease-in-out" placeholder="{PLACEHOLDER}" />
      </label>
      <textarea class="w-full rounded-2xl border border-[#4a6fa5]/20 bg-white/60 px-4 py-3 text-[#3a3a3a] placeholder:text-[#6f6a63] font-light shadow-[0_2px_10px_rgba(74,111,165,0.1)] focus:outline-none focus:shadow-[0_4px_20px_rgba(74,111,165,0.15)] focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5] transition-all duration-500 ease-in-out" rows="4" placeholder="{MESSAGE_PLACEHOLDER}"></textarea>
      <button type="submit" class="inline-flex items-center justify-center rounded-2xl px-6 py-3 shadow-[0_4px_20px_rgba(74,111,165,0.12)] hover:scale-[1.02] hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)] active:scale-[0.98] active:shadow-[inset_0_2px_10px_rgba(74,111,165,0.2)] transition-all duration-500 ease-in-out font-light bg-[#4a6fa5] text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4a6fa5] focus-visible:ring-offset-2 focus-visible:ring-offset-[#faf8f5] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:active:scale-100">
        {SUBMIT_TEXT}
      </button>
    </form>
  </div>
</section>
```

### 11.5 页脚

```html
<footer class="bg-[#f0ebe3] text-[#3a3a3a] border-t border-[#4a6fa5]/20 py-12 md:py-20 lg:py-28 px-4 md:px-8 lg:px-12">
  <div class="max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-10">
      <div>
        <span class="font-serif font-light tracking-wide text-[#3f628f] text-lg md:text-xl">{LOGO_TEXT}</span>
        <p class="mt-2 font-sans font-light text-xs md:text-sm text-[#3a3a3a]">{TAGLINE}</p>
      </div>
      <div>
        <h4 class="font-serif font-light tracking-wide text-[#3f628f] text-lg md:text-xl">{COLUMN_TITLE}</h4>
        <ul class="mt-3 font-sans font-light text-xs md:text-sm text-[#3a3a3a] space-y-2">
          <!-- 每个链接重复此结构；悬停用下划线，不用彩色小字 -->
          <li>
            <a href="#" class="underline-offset-4 transition-colors duration-500 ease-in-out hover:text-[#3f628f] hover:underline decoration-[#4a6fa5]/40">{LINK_TEXT}</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</footer>
```

---

## 12. 示例 Prompt

### 12.1 水彩画廊

```
用 Watercolor Style 创建一个艺术画廊页面：
1. 温暖纸张色背景 #faf8f5，叠加 2–3 个 blur-3xl 水彩晕染色块
2. 作品卡片使用半透明渐变（蜜桃/青绿）与大圆角
3. 标题使用 font-serif font-light，Hero 可加 italic
4. 悬停时同色系彩色阴影向外扩散，不做上浮
5. 动效 duration-500 ease-in-out，支持 reduced-motion
```

### 12.2 水彩个人主页

```
用 Watercolor Style 设计个人介绍页：
1. 全屏纸张底 + 多个水彩晕染色块，色块不得遮挡文字可读性
2. 导航使用轻半透明纸色（bg-[#faf8f5]/90），不做玻璃卡片
3. 联系方式卡片使用水彩渐变背景与柔和阴影
4. 小字只用 #3a3a3a / #3f628f / #6f6a63，符合 WCAG AA
5. 整体观感像一幅留白充足的水彩画
```

### 12.3 作品集

```
Create a portfolio showcase page using Watercolor Style:
- Warm paper background #faf8f5 with soft blurred watercolor washes
- Serif light headings, generous whitespace, 65–75ch line length
- Project cards with translucent peach/teal gradients and rounded-3xl corners
- Pigment-bloom hover shadows, no translate-y, duration-500 ease-in-out
- Accessible focus rings and prefers-reduced-motion fallback
```

---

## 13. 交付前自检清单

**输出代码前逐项验证；任何一项不通过，先修正再交付。**

### 13.1 Token 检查

- [ ] 按钮包含：`rounded-2xl`、`shadow-[0_4px_20px_rgba(74,111,165,0.12)]`、`hover:scale-[1.02]`、`hover:shadow-[0_10px_40px_...]`、`active:scale-[0.98]`、`transition-all duration-500 ease-in-out`、`font-light`
- [ ] 卡片包含：`rounded-2xl md:rounded-3xl`、`border border-[#4a6fa5]/20`、`shadow-[0_4px_20px_rgba(74,111,165,0.12)]`、`bg-[#faf8f5]`、`p-5 md:p-8`
- [ ] 输入框包含：`rounded-2xl`、`border border-[#4a6fa5]/20`、`bg-white/60`、`font-light`、`focus:shadow-[0_4px_20px_rgba(74,111,165,0.15)]`、`focus:outline-none`

### 13.2 禁止项检查

- [ ] 没有 `rounded-none` / `rounded-sm` / `rounded-md` / `rounded-lg`
- [ ] 没有 `border-black` / `border-2` / `border-4` / `border-l-4` / `border-r-4`
- [ ] 没有 `shadow-[2px_2px_0px...]` 等硬偏移阴影
- [ ] 没有 `font-black` / `font-bold` / `font-semibold` / `font-extrabold`
- [ ] 没有 `bg-black` / `bg-[#1a1a1a]` / `text-black`
- [ ] 没有低于 500ms 的交互过渡、`ease-linear` / `ease-in` / `ease-out`、bounce/elastic
- [ ] 没有悬停 `translate-y` 上浮

### 13.3 风格规则检查

- [ ] 使用柔和渐变或半透明色模拟水彩渗透
- [ ] 使用温暖纸张色 `bg-[#faf8f5]`，区块可用 `bg-[#f0ebe3]`
- [ ] 使用 `rounded-2xl` / `rounded-3xl` / `rounded-full` 柔化边缘
- [ ] 使用低透明度、柔和扩散的阴影
- [ ] 标题使用衬线字体，Hero/引文可加 italic；正文无粗体
- [ ] 颜色只来自水彩调色板，没有引入第二套近似色
- [ ] 正文行宽不超过 65–75 个字符

### 13.4 风格漂移检查

- [ ] 没有紫色到蓝色的渐变
- [ ] 没有渐变文字（`bg-clip-text text-transparent`）
- [ ] 没有把玻璃态当作默认风格
- [ ] 没有嵌套卡片
- [ ] 没有单侧粗边框装饰
- [ ] 没有 tiny uppercase tracked eyebrow
- [ ] 没有彩色背景上的灰色小字
- [ ] 没有过度饱和或刺眼的颜色
- [ ] 结果仍然能一眼识别为水彩画风

### 13.5 通用交付检查

- [ ] 响应式布局在手机、平板、桌面稳定，没有横向溢出
- [ ] 所有交互元素有可见焦点与可访问名称
- [ ] 文本对比度达到 WCAG AA，且没有用颜色单独传递状态
- [ ] 所有动效有 `prefers-reduced-motion` / `motion-reduce:` 备选
- [ ] 装饰性色块均带 `aria-hidden="true"` 与 `pointer-events-none`

---

## 14. 规范裁决记录（维护者用）

原风格文本存在几处相互冲突的规则，本 Skill 采用以下裁决，生成代码时以本文件正文为准：

1. **缓动时长**：原文 Token 字典写 `duration-400 ease-out`，动效规则又强制 `duration-500 ease-in-out` 且禁止快速缓动。统一为 `duration-500 ease-in-out`；`duration-400` 也不是 Tailwind v3 默认值。
2. **悬停阴影**：原文同时给出 `hover:shadow-[0_8px_30px_...0.2]` 与颜料晕开 `0_10_40 ... 0.35`。统一使用后者作为悬停反馈，前者仅作为常驻/聚焦阴影。
3. **弱化文字**：原文 `#8a8a8a` 在纸底上约 3.3:1，不满足 AA。正文改用 `#6f6a63`，`#8a8a8a` 只保留给装饰或大字。
4. **主按钮**：原文 `bg-[#4a6fa5]/80` 配白字约 3.5:1，不合规。主按钮改为实色 `bg-[#4a6fa5]`，保留半透明只用于晕染色块与次按钮边框。
5. **浅彩底小字**：新增深主色 `#3f628f`，解决 `#4a6fa5` 在 `#f0ebe3` 上仅约 4.3:1 的问题。
6. **字体斜体**：原文要求「衬线斜体」，模板又只写衬线。统一为标题 `font-serif font-light tracking-wide`，Hero/引文可加 `italic`；中文斜体效果差时只保留衬线。
7. **背景强调色**：原文另列 `#b4788c/#78a082/#c9a84c` 等近似色，统一收敛到四色水彩调色板，避免风格分散。
8. **字重**：原文只禁 `font-bold/black`，为保持轻盈感，同时禁用 `font-semibold/font-extrabold`。
