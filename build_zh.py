# -*- coding: utf-8 -*-
# Build Chinese localization files for Syncthing Windows Setup
# Outputs: Messages-zh.isl (UTF-8 BOM), zh-*.js (UTF-16 LE BOM), zh-README.rtf, zh-License.rtf
import re, os

DST = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- Messages-zh.isl
ISL = """\
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
"""
with open(os.path.join(DST, "Messages-zh.isl"), "w", encoding="utf-8-sig", newline="\r\n") as f:
    f.write(ISL)
print("Messages-zh.isl written")

# ---------------------------------------------------------------- zh-*.js
JS_BLOCKS = {
    "en-SetSyncthingConfig.js": """// BEGIN LOCALIZATION
var MSG_DLG_TITLE           = "Syncthing";
var MSG_SYNCTHING_NOT_FOUND = "未找到 syncthing.exe";
var MSG_SYNCTHING_ERROR     = "syncthing.exe 返回错误";
var MSG_CONFIG_NOT_FOUND    = "未找到文件：";
var MSG_CONFIG_NOT_UPDATED  = "无法更新 config.xml";
// END LOCALIZATION""",
    "en-SyncthingFirewallRule.js": """// BEGIN LOCALIZATION
var MSG_DLG_TITLE            = "Syncthing";
var MSG_QUERY_CREATE_RULE    = "要为 Syncthing 创建 Windows 防火墙规则吗？";
var MSG_QUERY_REMOVE_RULE    = "要删除 Syncthing 的 Windows 防火墙规则吗？";
var MSG_ERROR_DESC_NOT_FOUND = "（未找到错误描述）";
// END LOCALIZATION""",
    "en-SyncthingLogonTask.js": """// BEGIN LOCALIZATION
var MSG_DLG_TITLE            = "Syncthing";
var MSG_QUERY_CREATE         = "要创建登录时启动 Syncthing 的计划任务吗？";
var MSG_QUERY_REMOVE         = "要删除登录时启动 Syncthing 的计划任务吗？";
var MSG_TASK_NAME            = "登录时启动 Syncthing";
var MSG_ERROR_DESC_NOT_FOUND = "（未找到错误描述）";
// END LOCALIZATION""",
}
for src, block in JS_BLOCKS.items():
    text = open(os.path.join(DST, src), encoding="utf-8-sig").read()
    new_text, n = re.subn(r"// BEGIN LOCALIZATION.*?// END LOCALIZATION",
                          lambda m, b=block: b, text, flags=re.S)
    assert n == 1, src
    out = os.path.join(DST, src.replace("en-", "zh-", 1))
    open(out, "w", encoding="utf-16", newline="\r\n").write(new_text)
    print(os.path.basename(out), "written (UTF-16 LE)")

# ---------------------------------------------------------------- RTF builder
def esc(s):
    out = []
    for ch in s:
        o = ord(ch)
        if ch == "\t":
            out.append("\\t ")
        elif o < 128:
            out.append("\\" + ch if ch in "\\{}" else ch)
        else:
            cp = o - 65536 if o > 32767 else o
            out.append("\\u%d?" % cp)
    return "".join(out)

RTF_HEAD = (r"{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang2052"
            r"{\fonttbl{\f0\fnil\fcharset134 SimSun;}{\f1\fnil\fcharset0 Arial;}}"
            r"{\colortbl ;\red255\green255\blue255;\red248\green249\blue250;}"
            r"{\*\generator SyncthingSetupLoc}\viewkind4\uc1")
P = r"\pard\hyphpar0\widctlpar\kerning1\fs20\lang2052\par"

def para(ctl, bold, text):
    b = r"\b " if bold else r"\b0 "
    return r"\pard\hyphpar0\widctlpar\kerning1%s%s%s\par" % (ctl, b, esc(text))

def build_rtf(paras):
    body = [RTF_HEAD]
    for ctl, bold, text in paras:
        body.append(para(ctl, bold, text))
        body.append(P)
    body.append("}")
    return "".join(body)

IND1 = r"\fi-720\li720\kerning0"    # numbered heading (hanging indent)
IND2 = r"\li720\kerning0"           # body under heading
IND3 = r"\fi-720\li1440\kerning0"   # (a)/(b) items
CENTER = r"\qc\kerning0"
BOX = r"\cbpat2\li720\ri720\kerning0\highlight2"

# ---- zh-README.rtf
readme = [
    (CENTER, True, "关于 Syncthing"),
    (r"\sa200\sl240\slmult1\kerning0", False,
     "Syncthing 是一款持续文件同步程序。它在两台或多台计算机之间同步文件。我们致力于实现下列目标。目标按重要性排序，最重要的排在最前。这是目标列表的摘要版本。"),
    (r"\sa200\sl240\slmult1\kerning0", False, "Syncthing 应当："),
    (r"\fi-360\li360\sa200\sl240\slmult1\kerning0", True, "1.\t 防止数据丢失"),
    (r"\li360\sa200\sl240\slmult1\kerning0", False, "保护用户的数据至关重要。我们采取一切合理的预防措施，避免损坏用户的文件。"),
    (r"\fi-360\li360\sa200\sl240\slmult1\kerning0", True, "2.\t 防范攻击者"),
    (r"\li360\sa200\sl240\slmult1\kerning0", False, "同样，保护用户的数据至关重要。无论其他目标如何，我们绝不能让用户的数据面临被未经授权方窃听或修改的风险。"),
    (r"\fi-360\li360\sa200\sl240\slmult1\kerning0", True, "3.\t 易于使用"),
    (r"\li360\sa200\sl240\slmult1\kerning0", False, "Syncthing 应当亲切实用、易于理解、包容开放。"),
    (r"\fi-360\li360\sa200\sl240\slmult1\kerning0", True, "4.\t 自动化"),
    (r"\li360\sa200\sl240\slmult1\kerning0", False, "仅在绝对必要时才需要用户操作。"),
    (r"\fi-360\li360\sa200\sl240\slmult1\kerning0", True, "5.\t 普遍可用"),
    (r"\li360\sa200\sl240\slmult1\kerning0", False, "Syncthing 应当能在所有常见计算机上运行。我们深知并非每个人都能获得最新技术。"),
    (r"\fi-360\li360\sa200\sl240\slmult1\kerning0", True, "6.\t 面向个人"),
    (r"\li360\sa200\sl240\slmult1\kerning0", False, "Syncthing 的主要目标是让个人用户拥有安全、可靠且易于使用的文件同步。"),
    (r"\fi-360\li360\sa200\sl240\slmult1\kerning0", True, "7.\t 其他一切"),
    (r"\li360\sa200\sl240\slmult1\kerning0", False, "我们关心的许多事情并未列入此清单。只要不与上述目标冲突，为这些价值进行优化并没有问题。"),
]
open(os.path.join(DST, "zh-README.rtf"), "w", encoding="ascii", newline="\r\n").write(build_rtf(readme))
print("zh-README.rtf written")

# ---- zh-License.rtf (MPL 2.0, 简体中文译文)
lic = [
    (CENTER, True, "Mozilla 公共许可证（中文参考译文）"),
    (CENTER, False, "版本 2.0"),
    (IND2, False, "说明：以下为 Mozilla 公共许可证 2.0 版的简体中文参考译文，仅供参考；如中英文存在歧义，以英文原文为准。"),
    (IND1, True, "1.\t 定义"),
    (IND1, True, "1.1.\t “贡献者”（Contributor）"),
    (IND2, False, "指创建、参与创建或拥有本许可证下“被覆盖软件”的个人或法律实体。"),
    (IND1, True, "1.2.\t “贡献者版本”（Contributor Version）"),
    (IND2, False, "指其他人的贡献（如有）与该贡献者本人的贡献之组合。"),
    (IND1, True, "1.3.\t “贡献”（Contribution）"),
    (IND2, False, "指特定贡献者的被覆盖软件。"),
    (IND1, True, "1.4.\t “被覆盖软件”（Covered Software）"),
    (IND2, False, "指初始贡献者已附加附录 A 中声明的源代码形式、该源代码形式的可执行形式，以及对源代码形式的修改，各种情形均包括其中的一部分。"),
    (IND1, True, "1.5.\t “与次级许可证不兼容”（Incompatible With Secondary Licenses）"),
    (IND2, False, "指："),
    (IND3, False, "(a)\t 初始贡献者已在被覆盖软件上附加附录 B 所述的声明；或"),
    (IND3, False, "(b)\t 被覆盖软件是依据本许可证 1.1 版或更早版本的条款提供的，且未同时依据次级许可证的条款提供。"),
    (IND1, True, "1.6.\t “可执行形式”（Executable Form）"),
    (IND2, False, "指作品源代码形式以外的任何形式。"),
    (IND1, True, "1.7.\t “更大作品”（Larger Work）"),
    (IND2, False, "指将被覆盖软件与其他不属于被覆盖软件的材料（在一个或多个独立文件中）组合而成的作品。"),
    (IND1, True, "1.8.\t “许可证”（License）"),
    (IND2, False, "指本文件。"),
    (IND1, True, "1.9.\t “可许可”（Licensable）"),
    (IND2, False, "指在初始授予时或之后，有权在最大可能范围内授予本许可证所授予的任何及所有权利。"),
    (IND1, True, "1.10.\t “修改”（Modifications）"),
    (IND2, False, "指以下任一情形："),
    (IND3, False, "(a)\t 对被覆盖软件的内容进行增加、删除或修改而产生的源代码形式的任何文件；或"),
    (IND3, False, "(b)\t 包含任何被覆盖软件的任何新的源代码形式文件。"),
    (IND1, True, "1.11.\t 贡献者的“专利权利要求”（Patent Claims）"),
    (IND2, False, "指该贡献者可许可的任何专利中的权利要求（包括但不限于方法、流程和装置权利要求）——若非本许可证的授予，制作、使用、销售、许诺销售、制造、进口或转让其贡献或其贡献者版本的行为将侵犯这些权利要求。"),
    (IND1, True, "1.12.\t “次级许可证”（Secondary License）"),
    (IND2, False, "指 GNU 通用公共许可证第 2.0 版、GNU 宽通用公共许可证第 2.1 版、GNU Affero 通用公共许可证第 3.0 版，或上述许可证的任何后续版本。"),
    (IND1, True, "1.13.\t “源代码形式”（Source Code Form）"),
    (IND2, False, "指作品的首选修改形式。"),
    (IND1, True, "1.14.\t “您”（You，或 Your）"),
    (IND2, False, "指根据本许可证行使权利的个人或法律实体。就法律实体而言，“您”包括控制、受控于或与您共同受控于同一主体的任何实体。就本定义而言，“控制”指：(a) 通过合同或其他方式直接或间接主导该实体的方向或管理的权力；或 (b) 拥有该实体超过百分之五十（50%）的已发行股份或实益所有权。"),
    (IND1, True, "2.\t 许可授予与条件"),
    (IND1, True, "2.1.\t 授予"),
    (IND2, False, "每位贡献者特此授予您一项全球性的、免版税的、非排他性的许可："),
    (IND3, False, "(a)\t 依据该贡献者可许可的知识产权（专利和商标除外），以未修改形式、经修改形式或作为更大作品的一部分，使用、复制、提供、修改、展示、表演、分发以及以其他方式利用其贡献；以及"),
    (IND3, False, "(b)\t 依据该贡献者的专利权利要求，制作、使用、销售、许诺销售、制造、进口以及以其他方式转让其贡献或其贡献者版本。"),
    (IND1, True, "2.2.\t 生效日期"),
    (IND2, False, "第 2.1 节就某项贡献授予的许可，自贡献者首次分发该项贡献之日起生效。"),
    (IND1, True, "2.3.\t 授予范围的限制"),
    (IND2, False, "本第 2 节授予的许可是本许可证下授予的全部权利。不得依据本许可证下被覆盖软件的分发或许可，推定任何额外的权利或许可。尽管有上述第 2.1(b) 节的规定，贡献者不就下列情形授予专利许可："),
    (IND3, False, "(a)\t 针对贡献者已从被覆盖软件中移除的任何代码；或"),
    (IND3, False, "(b)\t 针对由下列原因造成的侵权：(i) 您或任何其他第三方对被覆盖软件的修改；或 (ii) 其贡献与其他软件的组合（作为其贡献者版本的一部分的除外）；或"),
    (IND3, False, "(c)\t 针对在没有其贡献的情况下会被被覆盖软件侵犯的专利权利要求。"),
    (IND2, False, "本许可证不授予任何贡献者的商标、服务标记或标志上的任何权利（为遵守第 3.4 节通知要求所必需的除外）。"),
    (IND1, True, "2.4.\t 后续许可证"),
    (IND2, False, "若您选择依据本许可证的后续版本（见第 10.2 节）或次级许可证的条款（如第 3.3 节所允许）分发被覆盖软件，任何贡献者均不因此作出额外授予。"),
    (IND1, True, "2.5.\t 声明"),
    (IND2, False, "每位贡献者声明，其相信其贡献为其原创作品，或其拥有足够的权利依据本许可证授予与其贡献相关的权利。"),
    (IND1, True, "2.6.\t 合理使用"),
    (IND2, False, "本许可证无意限制您依据适用的合理使用、公平交易或其他同等版权原则所享有的任何权利。"),
    (IND1, True, "2.7.\t 条件"),
    (IND2, False, "第 3.1、3.2、3.3 和 3.4 节是第 2.1 节所授予许可的条件。"),
    (IND1, True, "3.\t 责任"),
    (IND1, True, "3.1.\t 源代码形式的分发"),
    (IND2, False, "以源代码形式分发被覆盖软件（包括您创建或参与贡献的任何修改）时，必须依据本许可证的条款。您必须告知接收者：被覆盖软件的源代码形式受本许可证条款约束，以及他们如何获得本许可证的副本。您不得试图更改或限制接收者在源代码形式下享有的权利。"),
    (IND1, True, "3.2.\t 可执行形式的分发"),
    (IND2, False, "若您以可执行形式分发被覆盖软件，则："),
    (IND3, False, "(a)\t 该被覆盖软件还必须以源代码形式提供（如第 3.1 节所述），且您必须及时、以合理方式告知可执行形式的接收者如何获得该源代码形式的副本，收费不得超过向接收者分发的成本；以及"),
    (IND3, False, "(b)\t 您可以依据本许可证的条款分发该可执行形式，或以不同条款进行再许可，但前提是可执行形式的许可不得试图限制或改变接收者在本许可证下对源代码形式享有的权利。"),
    (IND1, True, "3.3.\t 更大作品的分发"),
    (IND2, False, "您可以按您选择的条款创建和分发更大作品，前提是您同时遵守本许可证对被覆盖软件的要求。如果更大作品是被覆盖软件与受一项或多项次级许可证约束的作品的组合，且该被覆盖软件并非“与次级许可证不兼容”，则本许可证允许您依据该次级（各）许可证的条款额外分发该被覆盖软件，使更大作品的接收者可以自行选择依据本许可证或该次级（各）许可证的条款进一步分发被覆盖软件。"),
    (IND1, True, "3.4.\t 通知"),
    (IND2, False, "您不得删除或更改被覆盖软件源代码形式中所含任何许可通知（包括版权声明、专利声明、担保免责声明或责任限制）的实质内容，但为纠正已知事实错误所必需的更改除外。"),
    (IND1, True, "3.5.\t 附加条款的适用"),
    (IND2, False, "您可以选择向被覆盖软件的一个或多个接收者提供担保、支持、赔偿或责任承担服务，并就此收费。但是，您只能以自己的名义（而非任何贡献者的名义）这样做。您必须绝对清楚地表明：任何此类担保、支持、赔偿或责任承担仅由您提供。且您特此同意，就您所提供的担保、支持、赔偿或责任条款导致任何贡献者承担的任何责任，向该贡献者作出赔偿。您可以加入针对特定司法管辖区的额外免责声明和责任限制。"),
    (IND1, True, "4.\t 因法律或法规而无法遵守"),
    (IND2, False, "若因法律、司法命令或法规，您无法就部分或全部被覆盖软件遵守本许可证的任何条款，则您必须：(a) 在最大可能范围内遵守本许可证的条款；且 (b) 说明相关限制及其影响的代码。该说明必须置于随本许可证下被覆盖软件全部分发包一同提供的文本文件中。除法律或法规禁止外，该说明必须足够详细，使具备一般技能的接收者能够理解。"),
    (IND1, True, "5.\t 终止"),
    (IND1, True, "5.1.\tab"),
    (IND2, False, "若您未能遵守本许可证的任何条款，本许可证授予的权利将自动终止。但是，若您恢复遵守，则特定贡献者依据本许可证授予的权利将：(a) 暂时恢复，除非且直到该贡献者明确且最终终止您的授权；以及 (b) 持续恢复，前提是该贡献者在您恢复遵守后的 60 天内未以某种合理方式将不符合项通知您。此外，若该贡献者以某种合理方式将不符合项通知您、这是您首次收到该贡献者关于不遵守本许可证的通知、且您在收到通知后的 30 天内恢复遵守，则该贡献者对您的授权将持续恢复。"),
    (IND1, True, "5.2.\tab"),
    (IND2, False, "若您以主张专利侵权（不包括请求宣告性判决之诉、反诉和交叉诉讼）为由对任何实体提起诉讼，声称贡献者版本直接或间接侵犯任何专利，则本许可证第 2.1 节下任何及所有贡献者授予您的被覆盖软件权利即告终止。"),
    (IND1, True, "5.3.\tab"),
    (IND2, False, "在依据上述第 5.1 或 5.2 节终止的情形下，终止前由您或您的分销商依据本许可证有效授予的所有最终用户许可协议（分销商和转售商除外）在终止后继续有效。"),
    (IND1, True, "6.\t 担保免责声明"),
    (BOX, False, "被覆盖软件依据本许可证“按现状”提供，不附任何形式的担保，无论明示、默示或法定，包括但不限于关于被覆盖软件无缺陷、适于销售、适合特定用途或不侵权的担保。被覆盖软件在质量和性能方面的全部风险由您承担。如任何被覆盖软件在任一方面被证明存在缺陷，由您（而非任何贡献者）承担一切必要的维护、修理或更正费用。本免责声明构成本许可证的实质组成部分。唯有在本免责声明的前提下，方授权使用任何被覆盖软件。"),
    (IND1, True, "7.\t 责任限制"),
    (BOX, False, "在任何情形下、依任何法律理论（无论是侵权行为（包括过失）、合同还是其他），任何贡献者或依上述许可分发被覆盖软件的任何人均不对您承担任何直接、间接、特殊、附带或后果性损害的责任，包括但不限于利润损失、商誉损失、停工、计算机故障或失灵，以及任何其他商业损害或损失，即使该方已被告知发生此类损害的可能性。在适用法律禁止此种限制的范围内，本责任限制不适用于因该方过失导致的死亡或人身伤害责任。部分司法管辖区不允许排除或限制附带或后果性损害，因此上述排除与限制可能不适用于您。"),
    (IND1, True, "8.\t 诉讼"),
    (IND2, False, "与本许可证相关的任何诉讼，只能向被告主要营业地所在司法管辖区的法院提起，且该诉讼应适用该司法管辖区的法律（其法律冲突规范除外）。本节任何内容均不妨碍一方提出交叉诉讼或反诉。"),
    (IND1, True, "9.\t 杂项"),
    (IND2, False, "本许可证构成就其标的事项达成的完整协议。若本许可证的任何条款被认定不可执行，则仅在使其可执行所必需的范围内对该条款进行修改。任何规定合同语言应作不利于起草方解释的法律或法规，不得用于作出不利于贡献者的解释。"),
    (IND1, True, "10.\t 本许可证的版本"),
    (IND1, True, "10.1.\t 新版本"),
    (IND2, False, "Mozilla 基金会是本许可证的管理者。除第 10.3 节规定外，管理者以外的任何人无权修改或发布本许可证的新版本。每个版本都将被赋予一个区别性的版本号。"),
    (IND1, True, "10.2.\t 新版本的效果"),
    (IND2, False, "您可以依据您最初收到被覆盖软件时所适用的本许可证版本的条款分发被覆盖软件，也可以依据许可证管理者发布的任何后续版本的条款分发被覆盖软件。"),
    (IND1, True, "10.3.\t 修改版本"),
    (IND2, False, "如果您创建不受本许可证约束的软件，并且希望为该软件创建新的许可证，您可以创建并使用本许可证的一个版本，前提是您对该许可证重新命名，并删除任何对许可证管理者名称的引用（为注明该修改后的许可证与本许可证存在差异而保留的除外）。"),
]
lic += [
    (IND2, False, "如果您创建不受本许可证约束的软件，并且希望为该软件创建新的许可证，您可以创建并使用本许可证的一个版本，前提是您对该许可证重新命名，并删除任何对许可证管理者名称的引用（为注明该修改后的许可证与本许可证存在差异而保留的除外）。"),
    (IND1, True, "10.4.\t 分发“与次级许可证不兼容”的源代码形式"),
    (IND2, False, "若您选择依据本许可证本版本的条款分发“与次级许可证不兼容”的源代码形式，则必须附加本许可证附录 B 所述的声明。"),
    (IND1, True, "附录 A - 源代码形式许可证声明"),
    (IND2, False, "本源代码形式受 Mozilla 公共许可证 2.0 版（MPL v. 2.0）条款的约束。如果未随本文件分发 MPL 的副本，您可以从 https://mozilla.org/MPL/2.0/ 获取一份。"),
    (IND2, False, "如无法或不便在特定文件中放置该声明，您可以将声明置于接收者通常会查找此类声明的位置（例如相关目录中的 LICENSE 文件）。"),
    (IND2, False, "您可以添加其他准确的版权所有权声明。"),
    (IND1, True, "附录 B - “与次级许可证不兼容”声明"),
    (IND2, False, "本源代码形式属于 Mozilla 公共许可证 2.0 版所定义的“与次级许可证不兼容”的源代码形式。"),
]
open(os.path.join(DST, "zh-License.rtf"), "w", encoding="ascii", newline="\r\n").write(build_rtf(lic))
print("zh-License.rtf written")
