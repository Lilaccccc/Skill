---
name: watercolor-style
description: "Watercolor（水彩画风）UI 设计系统 Skill。当用户要求生成水彩风/水彩画风/Watercolor Style、style_slug watercolor-style 的网页、着陆页或组件，或要求暖纸色背景 #faf8f5、柔和 radial-gradient 晕染、半透明水彩色、大圆角、衬线标题时使用。提供精确 Token 字典、颜料晕开/湿纸交互规则、页面骨架模板、禁止项清单与交付前自检流程，防止风格漂移。"
---

# Watercolor（水彩画风）Style Skill

模拟水彩画的设计系统：暖纸色底、半透明水彩色层层叠加、blur 色块晕染、大圆角软边缘、衬线标题与缓慢的液态交互。适合品牌站、作品集、画廊、博客、个人主页与表单页；不适合高密度后台表格。

## 什么时候使用

- 用户要求生成「水彩风 / 水彩画风 / Watercolor Style」页面或组件
- 用户要求按 style_slug `watercolor-style` 生成代码
- 用户给出艺术、手作、花艺、咖啡、疗愈、婚礼等需求，并希望温暖柔和的视觉语言

## 工作流程

1. **完整读取规范**：先读取 `references/style-reference.md`，获取配色、Token 字典、特效配方、页面模板与自检清单。不要凭记忆套用。
2. **逐字套用 Token**：按钮、卡片、输入框的必须项按规范逐字使用；颜色只从水彩调色板取。
3. **交付前自检**：按规范末尾清单逐项核对；任何一项不通过，修正后再交付。

## 最高优先级规则

- 背景：温暖纸张色 `bg-[#faf8f5]`，辅色 `bg-[#f0ebe3]`
- 水彩色只做半透明叠加：蜜桃 `#e8a87c`、青绿 `#85cdca`、玫瑰 `#c38d94`、沙色 `#d4a373`
- 柔化一切边缘：卡片 `rounded-2xl md:rounded-3xl`，按钮/输入框 `rounded-2xl`，色块 `rounded-full`
- 标题 `font-serif font-light tracking-wide`，Hero/引文可加 `italic`；正文 `font-sans font-light`
- 交互：`transition-all duration-500 ease-in-out`；悬停用同色系彩色阴影向外晕开，禁止 translate-y 上浮
- 禁止：硬边框、纯黑背景、直角、高饱和/霓虹色、粗重字重、快速缓动、渐变文字

## 核心 Token 速查

- 按钮：`rounded-2xl shadow-[0_4px_20px_rgba(74,111,165,0.12)] hover:scale-[1.02] transition-all duration-500 ease-in-out font-light bg-[#4a6fa5] text-white`
- 卡片：`rounded-2xl md:rounded-3xl border border-[#4a6fa5]/20 shadow-[0_4px_20px_rgba(74,111,165,0.12)] bg-[#faf8f5] p-5 md:p-8`
- 输入框：`rounded-2xl border border-[#4a6fa5]/20 bg-white/60 font-light focus:shadow-[0_4px_20px_rgba(74,111,165,0.15)] focus:outline-none`

## 交互四律

1. **颜料晕开**：悬停让同色系大阴影向外扩散（`hover:shadow-[0_10px_40px_rgba(74,111,165,0.35)]`），不做生硬上浮。
2. **湿纸效果**：悬停时卡片渐变底色微微加深（`from-…/20` → `hover:from-…/30`）。
3. **液态缓动**：一律 `duration-500 ease-in-out`，禁止低于 500ms 的交互过渡与 `ease-linear`。
4. **柔和按压**：`active:scale-[0.98]` 配合内阴影加深，不用弹簧回弹。

## 详细规范

配色对比度约束、特效配方、组件模板、错误对比与完整自检清单见 `references/style-reference.md`。
