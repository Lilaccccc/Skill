---
name: scalajs-vite-starter
description: 创建 Scala.js + Vite + sbt 前端项目脚手架（Scala 3、Laminar 响应式框架、ES 模块热更新）。当用户要求创建、初始化、搭建 Scala.js / ScalaJS 项目，或需要配置 vite-plugin-scalajs、sbt-scalajs、Scala.js 与 Vite 集成、scalajs:main.js 导入、Scala.js 模块热更新（SmallModulesFor）时使用。
---

# Scala.js + Vite 项目脚手架

通过 Vite（Vanilla 模板）+ sbt + Scala.js 插件搭建 Scala 3 前端项目，使用 Laminar 响应式框架，支持 ES 模块热更新。

官方文档：https://www.scala-js.org/

## 前置询问（必须）

每次创建项目前，先询问用户两个信息，后续用于替换模板占位符：

1. **项目名称** → 替换 `{{PROJECT_NAME}}`（写入 `build.sbt` 的 `name` 设置）
2. **热更新包名** → 替换 `{{HOT_RELOAD_PACKAGE}}`（写入 `build.sbt` 的 `SmallModulesFor(List(...))`，并作为 `MainApp.scala` 的包目录名）

## 创建流程

### 1. 创建 Vite Vanilla 模板

```bash
npm create vite@latest <项目目录名> -- --template vanilla
cd <项目目录名>
```

等价于交互式选择：framework = Vanilla，variant = JavaScript。

### 2. 安装 Scala.js Vite 插件

```bash
npm install -D @scala-js/vite-plugin-scalajs@latest
```

### 3. 复制模板文件

模板位于 `assets/template/`，复制到项目根目录（Vite 模板中已存在的同名文件直接覆盖）：

| 模板文件 | 目标位置 | 占位符替换 |
|---|---|---|
| `vite.config.js` | `vite.config.js` | 无 |
| `main.js` | `main.js`（覆盖模板自带文件） | 无 |
| `build.sbt` | `build.sbt` | `{{PROJECT_NAME}}`、`{{HOT_RELOAD_PACKAGE}}` |
| `project/build.properties` | `project/build.properties` | 无 |
| `project/plugins.sbt` | `project/plugins.sbt` | 无 |
| `src/main/scala/Main.scala` | `src/main/scala/Main.scala` | 无 |
| `src/main/scala/MainApp.scala.tpl` | `src/main/scala/<热更新包名>/MainApp.scala` | 无（目录名即包名） |

注意：

- `vite.config.js` 包含 sbt 2.x 产物目录兜底逻辑（官方插件会把 sbtn 输出的 ANSI 终端控制序列误当路径，导致 `Failed to load url /main.js`），不要简化或替换为裸 `scalaJSPlugin()`。
- `index.html` 中需保留 `<div id="app"></div>`，Vite Vanilla 模板默认已包含。
- `project/metals.sbt` 可选（Metals IDE 会自动生成，可留空）。

### 4. 安装依赖

```bash
npm install
```

### 5. 启动开发

需要两个进程同时运行：

```bash
sbt ~fastLinkJS    # 持续编译 Scala.js 产物
npm run dev        # Vite 开发服务器（0.0.0.0:5173）
```

## 可选：Windows 启动脚本

> 需要用户自行下载 Sbt ZIP 包：[Download | sbt](https://www.scala-sbt.org/download/).

若用户需要免装 sbt 的启动方式，提供以下两个 `.bat` 模板（路径中的 JDK 与 sbt 发行版目录需按用户环境替换）：

`start.bat`（持续编译）：

```bat
@echo off
"<JDK路径>\bin\java.exe" -jar "<项目根目录>\sbt-2.0.9\bin\sbt-launch.jar" ~fastLinkJS %*
```

`sbt.bat`（sbt 命令入口）：

```bat
@echo off
set "SBT_HOME=%~dp0sbt-2.0.9"
"<项目根目录>\sbt-2.0.9\bin\sbt.bat" %*
```
