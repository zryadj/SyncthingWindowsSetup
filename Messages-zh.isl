; Messages-zh.isl - 简体中文补充消息 (Simplified Chinese supplemental messages)
; File encoding: UTF-8 with byte-order marker (BOM)

[Messages]
PrivilegesRequiredOverrideTitle=选择安装模式
PrivilegesRequiredOverrideInstruction=选择安装模式
PrivilegesRequiredOverrideText1=%1 可以作为 Windows 服务为所有用户安装（需要管理员权限），也可以仅为当前用户安装。
PrivilegesRequiredOverrideText2=%1 可以仅为当前用户安装，也可以作为 Windows 服务为所有用户安装（需要管理员权限）。
PrivilegesRequiredOverrideAllUsers=为所有用户安装并作为 Windows 服务(&A)
PrivilegesRequiredOverrideAllUsersRecommended=为所有用户安装并作为 Windows 服务（推荐）(&A)
PrivilegesRequiredOverrideCurrentUser=仅为当前用户安装(&C)
PrivilegesRequiredOverrideCurrentUserRecommended=仅为当前用户安装（推荐）(&C)
FinishedLabel=[name] 已成功安装到您的计算机上。

[CustomMessages]
; Uninstall display
UninstallDisplayNamePerUserSuffix=（当前用户）
UninstallDisplayNameServiceSuffix=（服务）
; Service account
ServiceAccountDescription=Syncthing 服务账户
; Service
ServiceDisplayName=Syncthing 服务
ServiceDescription=Syncthing 可在两台或多台计算机之间实时、安全地同步文件。
; [Icons]
ShortcutNameConfigurationPage=Syncthing 配置页面
ShortcutNameConfigurationPageComment=打开 Syncthing 配置网页。
ShortcutNameStartSyncthing=启动 Syncthing
ShortcutNameStartSyncthingComment=启动 Syncthing。
ShortcutNameStopSyncthing=停止 Syncthing
ShortcutNameStopSyncthingComment=停止 Syncthing。
; [Tasks]
TasksStartAtBoot=系统启动时自动启动 Syncthing 服务(&A)
TasksStartServiceAfterInstall=安装完成后启动 Syncthing 服务(&I)
TasksStartAtLogon=登录时自动启动 Syncthing(&A)
TasksStartAtLogon_ACPowerOnly=仅在使用交流电源时才自动启动(&T)
TasksStartAfterInstall=安装完成后启动 Syncthing(&I)
TasksCreateDesktopIcon=创建指向 Syncthing 配置页面的桌面快捷方式(&D)
; [Run]
RunStatusMsg=正在完成安装任务...
RunPostInstallOpenConfigPage=打开 Syncthing 配置页面(&O)
; Initialization
InitializeSetupError0=安装初始化错误：不允许在域控制器上为所有用户安装。%n%n安装程序即将退出。
InitializeSetupError1=安装初始化错误：WSH 脚本注册无效。%n%n要解决此问题，请参阅文档中的“安装初始化错误”一节。%n%n安装程序即将退出。
InitializeSetupError2=安装初始化错误：检测到管理安装。%n%n安装程序检测到系统上已存在管理安装。若要重新安装，请使用 /ALLUSERS 命令行选项重新运行安装程序。%n%n安装程序即将退出。
InitializeSetupWarning0=警告：无法从 github.com 获取最新版本信息。
; Memo pages
MemoPage0Caption=许可证
MemoPage0Description=请参阅下方的许可证信息。
MemoPage0SubCaption=准备好继续安装时，请单击“下一步”。
; File pages
FilePage0Caption=选择安装 Zip 文件
FilePage0Description=安装程序应使用哪个 zip 文件来安装 Syncthing？
FilePage0SubCaption=指定安装 zip 文件的位置，然后单击“下一步”。
FilePage0Prompt=Syncthing 安装 zip 文件(&I)：
FilePage0Filter=Zip 文件 (*.zip)|*.zip|所有文件 (*)|*
; File page errors
FilePage0Item0Empty=必须指定 Syncthing zip 文件的路径。
; Configuration pages
ConfigPage0Caption=选择配置设置
ConfigPage0Description=安装程序应如何配置 Syncthing？
ConfigPage0SubCaption=指定 Syncthing 配置设置，然后单击“下一步”。
ConfigPage0Item0=自动升级间隔，单位小时(&U)（0 为禁用；默认为 %1）：
ConfigPage0Item1=GUI 配置页面监听地址(&A)（默认为 %1）：
ConfigPage0Item2=GUI 配置页面监听端口(&P)（默认为 %1）：
ConfigPage0Item3=启用中继（'false' 或 'true'，默认为 '%1'）(&R)：
; Configuration page errors
ConfigPage0Item0NotValid=自动升级间隔必须在 0 到 65535 之间。
ConfigPage0Item1Empty=必须指定监听地址。
ConfigPage0Item2NotValid=监听端口必须在 1024 到 65535 之间。
ConfigPage0Item3NotValid=中继值必须是 'false' 或 'true'。
; Download pages
DownloadPageAbortedByUser=下载已中止。
; Ready memo page
ReadyMemoZipFileInfo=安装 zip 文件位置：
ReadyMemoInstallSettings=安装设置：
ReadyMemoInstallOnline=在线安装（下载并安装 %1）
ReadyMemoInstallOffline=离线安装（使用安装 zip 文件）
ReadyMemoInstallAdmin=为所有用户安装并作为 Windows 服务
ReadyMemoInstallAdminServiceAccountUserName=服务账户用户名：%1
ReadyMemoInstallCurrentUser=为当前用户安装（%1）
ReadyMemoConfigInfo=配置设置：
ReadyMemoConfigItem0Disabled=自动升级已禁用
ReadyMemoConfigItem0Enabled=每 %1 小时进行一次自动升级检查
ReadyMemoConfigItem1=GUI 配置页面监听地址为
ReadyMemoConfigItem2=GUI 配置页面监听端口为
ReadyMemoConfigItem3Disabled=中继已禁用
ReadyMemoConfigItem3Enabled=中继已启用
; Preparing to Install page
PrepareToInstallUninstallNeeded=安装程序检测到应先卸载当前已安装的版本。
PrepareToInstallUninstallSucceeded=已成功卸载当前安装的版本。
; Preparing to Install errors
PrepareToInstallErrorMessage0=安装程序无法卸载系统上当前安装的版本。要执行升级，必须先卸载当前安装的旧版本，然后才能安装此版本。
PrepareToInstallErrorMessage1=安装程序检测到已安装的版本（%1）比此版本（%2）更新。要执行降级，请先卸载已安装的版本，再安装此版本。
; DeinitializeUninstall
DeinitializeUninstallAppDirRemoveSucceeded=已删除目录：%1
DeinitializeUninstallAppDirRemoveFailed=无法删除目录：%1
; Misc.
RunCommandMessage=运行命令："%1" %2
ProcessCheckSucceededRunning=ProcessCheck.dll 中的 FindProcess 函数执行成功；"%1" 正在运行
ProcessCheckSucceededNotRunning=ProcessCheck.dll 中的 FindProcess 函数执行成功；"%1" 未在运行
ProcessCheckFailed=ProcessCheck.dll 中的 FindProcess 函数执行失败
InstallTypeNotInstalled=未检测到该软件包已安装。
InstallTypeAdmin=检测到该软件包以管理模式安装。
InstallTypeNonAdmin=检测到该软件包以非管理模式安装。
DownloadFileSucceeded=下载成功
ZipFilePathFound=已找到指定的 zip 文件。
ZipFilePathNotFound=未找到指定的 zip 文件。
ZipFileNotValid=指定的 zip 文件无效。
InstalledVersion=已成功安装版本 %1
FileDeleteSucceeded=已删除文件：%1
FileDeleteFailed=无法删除文件：%1
