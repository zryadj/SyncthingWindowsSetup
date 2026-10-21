<!-- omit in toc -->
# Syncthing Windows Setup — 简体中文说明

> **[English](README.md) | 简体中文**

本仓库是 [Bill-Stewart/SyncthingWindowsSetup](https://github.com/Bill-Stewart/SyncthingWindowsSetup) 的**非官方增强分支**（上游采用 MPL-2.0 许可证，本分支沿用）。所有官方文档、版本历史与升级细节请参阅[英文 README](README.md)。

**声明**：本项目与 Syncthing 官方及上游作者无隶属关系；官方安装包请始终从[上游项目](https://github.com/Bill-Stewart/SyncthingWindowsSetup)获取。

---

## 目录

- [本分支改了什么](#本分支改了什么)
- [下载安装包](#下载安装包)
- [安装器使用要点](#安装器使用要点)
- [WebUI 主题安装（modern）](#webui-主题安装modern)
- [从源码构建](#从源码构建)
- [目录结构](#目录结构)
- [许可证](#许可证)

## 本分支改了什么

| 改动 | 说明 |
|---|---|
| 视觉升级 | 启用 Inno Setup 6.6+ 内置 **Polar** 主题（`WizardStyle=modern dynamic polar`），安装向导自动跟随系统深/浅色模式；另附 4 张自绘 Syncthing 品牌向导图（浅色/深色两套，可由 `gen_artwork.py` 重新生成） |
| 简体中文本地化 | 安装向导全量汉化（语言选择、信息页、许可证页、配置页、任务页、完成页）+ 三个 WSH 辅助脚本消息汉化；附 MPL-2.0 中文参考译文（`zh-License.rtf`，仅供参考，以英文原文为准） |
| 许可证页修复 | 修复多语言下许可证提取逻辑：按用户所选语言（`ActiveLanguage`）提取对应许可证文件，中文用户看到中文许可页 |
| WebUI 主题 | 附带 `webui-theme/modern`——Syncthing v2 网页管理界面的自定义浅色主题（品牌蓝 + 白卡片圆角 + 自托管 HarmonyOS Sans SC 字体），见下文安装说明 |
| 工具脚本 | `build_zh.py`（生成/更新全部中文文件）、`gen_artwork.py`（重新生成向导图片） |

对上游脚本逻辑的改动仅两处：`Syncthing.iss` 头部声明、`[Languages]`/许可证提取相关行；其余上游逻辑保持原样。

## 下载安装包

前往 [Releases](https://github.com/zryadj/SyncthingWindowsSetup/releases) 页面下载 `syncthing-windows-setup-v*.exe`。

版本号带 `-cn.x` 后缀的 Release 为本分支构建；不带后缀的版本对应上游官方发布。

## 安装器使用要点

- **在线安装（默认）**：安装时联网从 Syncthing 官方 GitHub Releases 下载对应架构的 Syncthing 本体。
- **离线安装**：先从 [syncthing releases](https://github.com/syncthing/syncthing/releases) 下载 `syncthing-windows-<版本>-<架构>.zip`，然后：

  ```bat
  syncthing-windows-setup-v2.1.1.exe /zipfilepath="D:\下载\syncthing-windows-amd64-v1.30.0.zip"
  ```

- 安装模式：可为**所有用户**安装（注册 Windows 服务，需要管理员权限，推荐），或**仅为当前用户**安装。
- 首次运行出现语言选择对话框；中文 Windows 会自动预选“简体中文”。
- 系统为深色模式时向导自动切换深色外观；也可用 `/NOSTYLE` 参数临时关闭主题样式。

## WebUI 主题安装（modern）

`webui-theme/` 是 [Syncthing](https://syncthing.net) 网页管理界面（`http://127.0.0.1:8384`）的自定义浅色主题：品牌蓝强调色（`#0891D1`）、白色圆角卡片、现代化选项卡与输入框，并**自托管 HarmonyOS Sans SC 字体**（Apache-2.0），中西文与数字字形统一。

适用于 **Syncthing v2.x**（在 v2.1.6 上实测）。主题是“稀疏”资产覆盖——只提供 `theme.css` 与字体，其余文件自动回退内置默认主题，因此 **Syncthing 升级不会使其失效**，也**不修改任何 Syncthing 文件**。

### 截图预览

| 主页 | 设置 |
|:---:|:---:|
| ![主页](https://cdn.jsdelivr.net/gh/zryadj/SyncthingWindowsSetup@main/webui-theme/screenshots/home.png) | ![设置](https://cdn.jsdelivr.net/gh/zryadj/SyncthingWindowsSetup@main/webui-theme/screenshots/settings.png) |

| 设备标识 |
|:---:|
| ![设备标识](https://cdn.jsdelivr.net/gh/zryadj/SyncthingWindowsSetup@main/webui-theme/screenshots/device-id.png) |

**安装步骤**：

1. 把 `webui-theme` 文件夹整个复制到任意位置，例如 `C:\syncthing-webui-theme`（保持其中的 `modern` 子目录结构）。
2. 设置环境变量（用户级），指向该文件夹：

   ```bat
   setx STGUIASSETS "C:\syncthing-webui-theme"
   ```

3. 重启 Syncthing（退出正在运行的 syncthing 进程——包括托盘/监控子进程——再重新启动；若以服务方式运行则重启服务）。
4. 打开网页管理界面：**操作 → 设置 → 常规 → 主题**，选择 **modern**，保存。
5. 浏览器强制刷新（Ctrl+F5）。

**卸载/回退**：在设置里把主题换回 *default* 或 *dark* 即可；彻底移除可删除环境变量后重启 Syncthing：

```bat
reg delete "HKCU\Environment" /v STGUIASSETS /f
```

> 提示：主题为固定浅色配色（深色系统下仍显示浅色）；原生 *dark*/*black* 主题仍可随时在设置中选用。

## 从源码构建

1. 安装 [Inno Setup](https://jrsoftware.org/isdl.php) **6.7.3 或更高版本**。
2. 简体中文界面需要 [ChineseSimplified.isl](https://github.com/jrsoftware/issrc/blob/main/Files/Languages/ChineseSimplified.isl)（Inno 6.7.3 默认不自带）——下载后放入 Inno 安装目录的 `Languages\` 文件夹。
3. 按 [building.md](building.md) 的说明，把 5 组辅助工具的 32 位/64 位版本分别放入 `binaries\i386\` 与 `binaries\x86_64\`：[asmt](https://github.com/Bill-Stewart/asmt/releases)、[ErrInfo](https://github.com/Bill-Stewart/ErrInfo)、[ServMan](https://github.com/Bill-Stewart/ServMan/releases)、[shawl](https://github.com/mtkennerly/shawl/releases)、[stctl](https://github.com/Bill-Stewart/stctl/releases)。
4. 编译：

   ```bat
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" Syncthing.iss
   ```

   产物为 `syncthing-windows-setup-v<版本>.exe`。

辅助脚本（可选）：

```bat
python build_zh.py      :: 重新生成全部中文文件（Messages-zh.isl / zh-*.js / zh-*.rtf）
python gen_artwork.py   :: 重新生成 4 张向导 PNG（需 Pillow）
```

## 目录结构

```
├── Syncthing.iss            Inno Setup 主脚本（含主题与双语集成）
├── Messages-en.isl / Messages-zh.isl   英文 / 简体中文补充消息
├── en-*.rtf / zh-*.rtf      信息页与许可证（RTF）
├── en-*.js / zh-*.js        安装后执行的 WSH 辅助脚本（防火墙规则、登录任务、配置）
├── syncthing-wizard-*.png   自绘向导图（浅色 / 深色）
├── webui-theme/modern/      Syncthing 网页界面 modern 主题
├── build_zh.py / gen_artwork.py   中文文件与向导图生成脚本
└── building.md              上游构建与本地化文档
```

## 许可证

- 安装器与上游脚本：[MPL-2.0](LICENSE)（本分支衍生文件同许可发布）
- HarmonyOS Sans SC 字体：[Apache-2.0](webui-theme/modern/assets/fonts/LICENSE-HarmonyOS-Sans.txt)（已随字体附带许可文本）
- 仓库内第三方二进制（jq.exe、unzip.exe、ProcessCheck.dll、UninsIS.dll）各自附带许可文件，均原样保留
- "Syncthing" 名称与logo归其各自权利人所有；本仓库为非官方第三方项目
