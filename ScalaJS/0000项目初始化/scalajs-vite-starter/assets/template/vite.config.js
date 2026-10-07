import {spawn} from "node:child_process";
import {existsSync} from "node:fs";
import {defineConfig} from "vite";
import scalaJSPlugin from "@scala-js/vite-plugin-scalajs";

const SCALAJS_URI_PREFIX = "scalajs:";

/*
 * sbt 2.x 通过 sbtn 薄客户端执行命令，stdout 末尾会带上终端控制序列（例如 ESC[0J）。
 * 官方插件把 `sbt print fastLinkJSOutput` 的最后一行当作 Scala.js 产物目录，
 * 此时拿到的是控制序列而不是路径，于是 'scalajs:main.js' 会被解析成非法路径，
 * Vite 报 Failed to load url /main.js。
 *
 * 这里保留官方插件的行为，只在它给出的路径磁盘上不存在时，自己重新取一次
 * 产物目录兜底（去掉 ANSI 转义序列后，取最后一个绝对路径行）。
 */
function scalaJSOutputDirFallback() {
  const official = scalaJSPlugin();
  let isDev = true;
  let outputDirPromise;

  function queryOutputDir() {
    const task = isDev ? "fastLinkJSOutput" : "fullLinkJSOutput";
    const args = ["--batch", "-no-colors", "-Dsbt.supershell=false", `print ${task}`];
    const isWindows = process.platform === "win32";
    const child = spawn(
      isWindows ? "sbt.bat" : "sbt",
      isWindows ? args.map((arg) => `"${arg}"`) : args,
      {shell: isWindows, stdio: ["ignore", "pipe", "inherit"]}
    );
    let stdout = "";
    child.stdout.setEncoding("utf-8");
    child.stdout.on("data", (data) => {
      stdout += data;
    });
    return new Promise((resolve, reject) => {
      child.on("error", reject);
      child.on("close", (code) => {
        const dir = stdout
          // 去掉 ANSI 转义序列
          .replace(/\u001b\[[0-9;?]*[A-Za-z]/g, "")
          .split(/\r?\n/)
          .map((line) => line.trim())
          // 只认绝对路径行（Windows 盘符或 Unix 根路径）
          .filter((line) => /^([A-Za-z]:[\\/]|\/)/.test(line))
          .pop();
        if (dir) resolve(dir.replace(/\\/g, "/"));
        else reject(new Error(`无法获取 Scala.js 产物目录（sbt 退出码 ${code}）`));
      });
    });
  }

  return {
    ...official,
    name: "scalajs:output-dir-fallback",
    configResolved(config) {
      isDev = config.mode === "development";
      return official.configResolved?.(config);
    },
    buildStart(...args) {
      return official.buildStart?.(...args);
    },
    async resolveId(source, importer, options) {
      const resolved = await official.resolveId?.(source, importer, options);
      if (typeof resolved !== "string" || existsSync(resolved)) {
        return resolved;
      }
      outputDirPromise ??= queryOutputDir();
      const outputDir = await outputDirPromise;
      return `${outputDir}/${source.slice(SCALAJS_URI_PREFIX.length)}`;
    },
  };
}

export default defineConfig({
  // 注册 Scala.js 插件
  plugins: [scalaJSOutputDirFallback()],
  server: {
    // 或 host: true，两者等价
    host: "0.0.0.0",
    port: 5173,
    strictPort: true
  }
});
