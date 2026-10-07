scalaVersion := "3.9.0"

lazy val root = project.in(file("."))
  // 启用 Scala.js 插件
  .enablePlugins(ScalaJSPlugin)
  .settings(
    // 设置 Scala 项目名称
    name := "{{PROJECT_NAME}}",

    // 通过 npm run dev 引入 scalajs:main.js 时自动调用 main 方法
    scalaJSUseMainModuleInitializer := true,

    // 设置热更新 sbt ~fastLinkJS
    scalaJSLinkerConfig ~= {
      _.withModuleKind(org.scalajs.linker.interface.ModuleKind.ESModule)
        .withModuleSplitStyle(org.scalajs.linker.interface.ModuleSplitStyle.SmallModulesFor(List("{{HOT_RELOAD_PACKAGE}}")))
    },

    // 引入 scala.js dom 与 laminar（响应式框架） 依赖
    libraryDependencies += "org.scala-js" %%% "scalajs-dom" % "2.8.1",
    libraryDependencies += "com.raquo" %%% "laminar" % "17.2.1"
    // laminar 路由依赖
    libraryDependencies += "org.felher" %% "laminouter" % "0.17.2",
    // JSON 序列化依赖
    libraryDependencies ++= Seq(
      "io.circe" %% "circe-core",
      "io.circe" %% "circe-generic",
      "io.circe" %% "circe-parser"
    ).map(_ % "0.14.1"),
    // Scala.js 使用 Java 时间库依赖
    libraryDependencies ++= Seq(
      "io.github.cquiroz" %% "scala-java-time-tzdb",
      "io.github.cquiroz" %% "scala-java-time"
    ).map(_ % "2.7.0"),
    // 线程上下文依赖，使用 import org.scalajs.macrotaskexecutor.MacrotaskExecutor.Implicits.*
    libraryDependencies += "org.scala-js" %% "scala-js-macrotask-executor" % "1.1.1",
  )
