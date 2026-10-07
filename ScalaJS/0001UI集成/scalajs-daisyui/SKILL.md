---
name: scalajs-daisyui
description: 为 Scala.js + Vite 项目接入 daisyUI（Tailwind CSS 4）样式库：安装依赖、配置 @tailwindcss/vite 插件与 style.css，在 Laminar 中使用 daisyUI 组件类。当用户要求给 Scala.js/ScalaJS 项目集成 daisyUI、Tailwind CSS 或 UI 组件库时使用。
---

# Scala.js 整合 daisyUI

在已有的 Scala.js + Vite 项目（见 `scalajs-vite-starter`）上接入 [daisyUI](https://daisyui.com/)。

关键前提：daisyUI 是 Tailwind CSS 的插件。daisyUI 5 需要搭配 **Tailwind CSS 4**，走 `@tailwindcss/vite` 插件，
**不需要 PostCSS，也不需要 `tailwind.config.js`**（v4 全部用 CSS 配置）。

## 1. 安装依赖

```bash
npm install tailwindcss@latest @tailwindcss/vite@latest daisyui@latest
```

## 2. 配置 Vite

在 `vite.config.js` 中**保留原有的 `scalaJSPlugin()`**，追加 `tailwindcss()`：

```js
import { defineConfig } from 'vite'
import scalaJSPlugin from '@scala-js/vite-plugin-scalajs'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [scalaJSPlugin(), tailwindcss()]
})
```

## 3. 配置样式入口

把样式入口文件（Vite Vanilla 模板为 `src/style.css`，由 `src/main.js` 通过 `import './style.css'` 引入）
**内容整体替换**为：

```css
@import "tailwindcss";
@plugin "daisyui";
```

> 模板自带的演示样式会与 Tailwind/daisyUI 冲突，建议直接清空替换，不要叠加。

## 4. 在 Laminar 中使用组件类

daisyUI 就是 CSS 类，直接在 `className` 里写即可：

```scala
package app

import com.raquo.laminar.api.L.*
import com.raquo.laminar.nodes.ReactiveHtmlElement
import org.scalajs.dom.HTMLDivElement

object MainApp {
  def appElement(): ReactiveHtmlElement[HTMLDivElement] = div(
    className := "card bg-base-100 shadow-xl  w-96",
    div(
      className := "card-body",
      h2(className := "card-title", "daisyUI + Scala.js"),
      div(
        className := "card-actions justify-end",
        button(className := "btn btn-primary", "Primary"),
        button(className := "btn btn-ghost", "Ghost")
      )
    )
  )
}
```

## 5. 验证

```bash
npm run dev
```

浏览器打开 `http://localhost:5173`，并确认编译后的样式包含 daisyUI：

- 请求 `http://localhost:5173/src/style.css` 应返回 200；
- 内容包含主题变量 `--color-base-100` 与 `[data-theme=...]` 定义；
- 在源码中写一个 daisyUI 类（如 `btn btn-primary`）后，产物 CSS 体积会明显增大并出现 `.btn` 规则。

可用如下命令快速自检（PowerShell）：

```powershell
$c = (Invoke-WebRequest -Uri "http://localhost:5173/src/style.css" -UseBasicParsing).Content
[bool]($c -match '--color-base-100'); [bool]($c -match '\.btn\s*\{')
```

## 注意事项与排错

- **按需生成**：Tailwind v4 只产出被源码扫描到的类名对应的 CSS。已实测 **`.scala` 源码会被自动扫描**，
  因此直接在 `MainApp.scala` 里写 `className := "btn btn-primary"` 即可生效，**无需额外配置 `@source`**。
  若类名是运行时拼接（如 `"btn-" + name`）则无法被扫描到，需改用完整字面量类名或显式 `@source`。
- **不要创建 `tailwind.config.js`**：v4 用 CSS 配置；混用会导致配置不生效。
- **主题 / 暗色模式**：daisyUI 5 在 CSS 里配置，例如
  `@plugin "daisyui" { themes: light --default, dark --prefersdark; }`；
  运行时通过给 `<html>` 设置 `data-theme` 属性切换。
- **Node 版本**：Vite 8 / Tailwind 4 要求 Node >= 20。若机器默认 Node 过旧（会连带 npm 报错），
  先用 nvm 切换：`nvm use <版本号>`。
- **改动 Vite 配置后**需要重启 `npm run dev`（配置文件不会热更新）。
- **与 Scala.js 产物共存**：`scalaJSPlugin()` 与 `tailwindcss()` 顺序无强依赖，但两者都要保留；
  `scalajs:main.js` 的引入方式不变。