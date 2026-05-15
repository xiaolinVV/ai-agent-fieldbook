# 浏览器自动化工具深度调研：Playwright、MCP、CLI 与 Agent 浏览器

调研日期：2026-05-14  
调研对象：

- https://github.com/epiral/bb-browser
- https://github.com/browser-use/browser-use
- https://github.com/microsoft/playwright-cli
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://github.com/vercel-labs/agent-browser
- https://github.com/microsoft/playwright
- https://github.com/microsoft/playwright-mcp
- https://github.com/microsoft/playwright-python

调研口径：

- 一手来源：GitHub 仓库 README、package.json、pyproject.toml、release、源码片段、官方安全/隐私说明。
- 包元数据：npm registry、PyPI。
- 仓库状态：GitHub REST API，数据抓取于 2026-05-14。
- 本报告没有做本地安装、跑通、压测或真实任务评测。没有验证就不装作验证过。

## 核心判断

这不是“8 个浏览器自动化工具谁最强”的问题。把它们放在同一张排行榜里，是错误的数据结构。

正确分层是：

1. 底层浏览器自动化内核：`microsoft/playwright`、`microsoft/playwright-python`
2. Agent 可调用接口层：`microsoft/playwright-cli`、`microsoft/playwright-mcp`、`ChromeDevTools/chrome-devtools-mcp`、`vercel-labs/agent-browser`、`epiral/bb-browser`
3. LLM 决策循环/Agent 框架：`browser-use/browser-use`

核心结论：

- 如果要做稳定、可复现、可测试的浏览器自动化，Playwright 仍然是基础设施，不要自己发明一套浏览器控制层。
- 如果是 coding agent 在本地开发/测试网页，优先看 CLI 类工具。CLI 的上下文成本低，失败面更窄。
- 如果是通用 MCP 客户端或长会话探索，`playwright-mcp` 是更标准的入口。
- 如果重点是 Chrome DevTools、性能、网络、console、memory、Lighthouse，`chrome-devtools-mcp` 是专门工具，不是 Playwright MCP 的简单替代。
- 如果重点是“复用真实浏览器登录态”和站点适配器，`bb-browser` 的方向很实用，但它的风险也正来自这里：它把用户真实浏览器变成了 Agent 的能力边界。
- 如果要直接让 LLM 自主完成网页任务，`browser-use` 是 Agent 框架，不只是浏览器工具。它更强，也更不确定。
- `agent-browser` 是一个很完整的 Rust 原生 CLI 方案，安全开关比多数 CLI 工具认真，但默认是 opt-in。默认 unrestricted 的工具不能直接塞进高风险自动化场景。

## 分层地图

| 层级 | 项目 | 本质 | 适合场景 | 不适合场景 |
|---|---|---|---|---|
| 浏览器自动化内核 | `microsoft/playwright` | Node/TS 生态的跨浏览器自动化和测试框架 | E2E 测试、可复现脚本、trace、跨浏览器验证 | 直接给 LLM 用，除非外面再包 CLI/MCP/Skill |
| 浏览器自动化内核 | `microsoft/playwright-python` | Python 版 Playwright 绑定 | Python 实验、数据采集脚本、课程/lab | Agent 交互层；它不是 MCP/CLI 工具 |
| Coding agent CLI | `microsoft/playwright-cli` | 面向 coding agent 的 Playwright CLI + skills | 本地网页测试、截图、trace、session dashboard | 非 coding-agent 的 MCP 长循环 |
| MCP 工具层 | `microsoft/playwright-mcp` | Playwright 的 MCP server | MCP 客户端、结构化 accessibility snapshot、长会话浏览器状态 | token 极度紧张的 coding agent 高频调用 |
| DevTools MCP | `ChromeDevTools/chrome-devtools-mcp` | Chrome DevTools 能力暴露给 MCP | 性能、console、network、Lighthouse、memory、Chrome 调试 | Firefox/WebKit；泛化跨浏览器测试 |
| Agent CLI | `vercel-labs/agent-browser` | Rust 原生 browser automation CLI | 快速 CLI、session/profile/auth vault、安全策略实验 | 需要跨浏览器一致性的测试基座 |
| 真实浏览器 API | `epiral/bb-browser` | 用本机真实 Chrome + 登录态 + site adapter 暴露网站能力 | 登录后资料收集、跨平台搜索、中文/社媒站点研究 | 严肃 E2E 测试、无状态 CI、敏感账号自动化 |
| LLM Agent 框架 | `browser-use/browser-use` | 浏览器 + LLM 决策循环 + cloud/SDK/CLI | 自主网页任务、表单、购物、个人助理原型 | 需要确定性、审计性、强可复现的流程 |

## 仓库与包状态

说明：`open_issues_count` 为 GitHub API 字段，不等于 bug 数。npm 下载量为 2026-04-13 到 2026-05-12 的 last-month 统计，npm 有统计延迟。

| 项目 | 语言 | License | Stars / Forks | open_issues_count | 最新发布 | 最近 push | 包状态 |
|---|---:|---:|---:|---:|---|---|---|
| `epiral/bb-browser` | TypeScript | MIT | 5,150 / 507 | 85 | `bb-browser-v0.11.6`, 2026-05-11 | 2026-05-11 | npm `bb-browser@0.11.6`，last-month 6,309 downloads |
| `browser-use/browser-use` | Python | MIT | 93,868 / 10,606 | 227 | `0.12.6`, 2026-04-02 | 2026-05-13 | PyPI `browser-use==0.12.6` |
| `microsoft/playwright-cli` | TypeScript | Apache-2.0 | 10,329 / 538 | 8 | `v0.1.13`, 2026-05-07 | 2026-05-07 | npm `@playwright/cli@0.1.13`，last-month 1,986,979 downloads |
| `ChromeDevTools/chrome-devtools-mcp` | TypeScript | Apache-2.0 | 39,559 / 2,508 | 96 | `chrome-devtools-mcp-v0.26.0`, 2026-05-12 | 2026-05-14 | npm `chrome-devtools-mcp@0.26.0`，last-month 6,163,267 downloads |
| `vercel-labs/agent-browser` | Rust | Apache-2.0 | 32,973 / 2,038 | 463 | `v0.27.0`, 2026-05-07 | 2026-05-13 | npm `agent-browser@0.27.0`，last-month 2,851,726 downloads |
| `microsoft/playwright` | TypeScript | Apache-2.0 | 88,680 / 5,686 | 168 | `v1.60.0`, 2026-05-11 | 2026-05-14 | npm `playwright@1.60.0`，last-month 211,808,698 downloads |
| `microsoft/playwright-mcp` | TypeScript | Apache-2.0 | 32,492 / 2,668 | 2 | `v0.0.75`, 2026-05-07 | 2026-05-12 | npm `@playwright/mcp@0.0.75`，last-month 9,818,490 downloads |
| `microsoft/playwright-python` | Python | Apache-2.0 | 14,632 / 1,157 | 18 | `v1.59.0`, 2026-04-29 | 2026-05-12 | PyPI `playwright==1.59.0` |

额外观察：

- `@playwright/cli@0.1.13` 和 `@playwright/mcp@0.0.75` 当前 package.json 依赖 `playwright` / `playwright-core` 的 `1.61.0-alpha-1778188671000`。这说明它们追随 Playwright 主干很近，功能新，但生产环境要 pin 版本并做回归。
- `browser-use` 依赖面很宽：LLM provider、MCP、PDF、docx、cloud SDK、CDP 相关包都在依赖列表里。它不是小工具，是框架。
- `agent-browser` 的 npm 包是原生 Rust binary 的分发入口；README 明确说 daemon 不需要 Playwright 或 Node.js。
- `chrome-devtools-mcp` 要求 Node.js `^20.19.0 || ^22.12.0 || >=23`，并官方支持 Chrome / Chrome for Testing，不承诺其他 Chromium 浏览器。

## 项目拆解

### 1. microsoft/playwright

一句话：这是底座。别把底座和 Agent 包装层混为一谈。

核心数据结构：

- `Browser`：浏览器进程。
- `BrowserContext`：隔离的会话/状态边界，相当于轻量浏览器 profile。
- `Page`：页面。
- `Locator`：稳定定位元素的抽象，优先按 role、label、placeholder、test id 这类用户语义定位。
- `Trace` / screenshot / video / network / console：失败复盘数据。

好品味：

- `BrowserContext` 把登录态、cookie、storage、隔离性放在一个清楚的结构里。很多浏览器工具烂就烂在状态边界含糊。
- locator 不是裸 CSS selector。面向用户语义的定位更稳定，少写脆弱特殊情况。
- auto-wait 和 web-first assertions 把“sleep 3 秒”这种垃圾条件消掉。
- 跨 Chromium、Firefox、WebKit 是实打实的工程价值。

风险：

- Playwright 本身不是 Agent 抽象。直接让 LLM 写 Playwright 代码，能用，但成本高、上下文重、失败恢复也要自己设计。
- 真实用户 profile 不是默认模型。它更偏隔离、可复现、测试友好。

适合本仓库学习：

- 必学。先用 Playwright 建立浏览器自动化的正确数据结构，再看上层 Agent 工具。

### 2. microsoft/playwright-python

一句话：Python 生态里的 Playwright，不是另一个新概念。

核心价值：

- 同一套 Chromium / Firefox / WebKit 自动化能力，给 Python 使用。
- 同时支持 sync 和 async API。
- PyPI 最新版本为 `1.59.0`，要求 Python `>=3.9`。

好品味：

- 对 Python 学习实验很友好。Agent fieldbook 里的 lab 很多会用 Python，直接用它比绕到 Node 更顺。
- 没有额外包装成“智能 Agent”，所以边界清楚。

风险：

- 如果研究主题是“Agent 如何观察页面、规划动作、恢复失败”，Playwright Python 只是底层库，不会替你解决 Agent 循环。

适合本仓库学习：

- 用它做最小可运行实验：打开页面、定位元素、保存 storage state、抓 trace、验证失败模式。

### 3. microsoft/playwright-cli

一句话：Playwright 给 coding agent 的 CLI 入口。它的核心卖点不是功能最多，而是 token 成本低。

核心设计：

- CLI 命令直接驱动 Playwright。
- 支持 sessions、persistent profile、snapshot、refs、selectors、Playwright locator、network mocking、console、requests、trace、video、dashboard。
- README 明确对比 CLI 与 MCP：coding agent 高频工具调用时，CLI 比 MCP 更省上下文。

好品味：

- “工具输出落文件，命令只回摘要/路径”是对 Agent 上下文窗口的尊重。
- session dashboard 是实用功能：人可以看到 agent 正在干什么，并接管。
- command surface 贴近 Playwright，不发明太多新概念。

风险：

- 项目很新。虽然背靠 Microsoft / Playwright，但 npm 包仍是 `0.1.x`。
- 当前依赖 Playwright alpha build。对实验没问题；生产链路必须 pin 并回归。

适合本仓库学习：

- 非常适合做“coding agent 如何用 CLI 驱动浏览器测试”的实验。
- 可以和 `playwright-mcp` 做同任务对照：token、速度、失败恢复、人类观察成本。

### 4. microsoft/playwright-mcp

一句话：标准 MCP 入口，让 LLM 通过 accessibility snapshot 操作浏览器。

核心设计：

- MCP server 封装 Playwright。
- LLM 看到结构化 accessibility tree，用 element ref 操作页面，不依赖视觉模型。
- 支持 persistent profile、isolated session、storage state、CDP endpoint、browser selection、network/console 配置、Docker、HTTP transport。

好品味：

- MCP 对“长会话、持续状态、工具发现”很自然。
- accessibility snapshot 比截图更确定，更省推理歧义。
- 配置项完整，能接现有 browser endpoint，也能起独立 profile。

风险：

- README 明确说它不是安全边界。不能因为它是 MCP 就把真实账号和敏感页面交给它乱跑。
- MCP 工具 schema 和页面树会消耗上下文。coding agent 一边读代码一边测网页时，可能不如 CLI 干净。
- 同样依赖当前 Playwright alpha build。

适合本仓库学习：

- 适合研究 MCP 工具调用、状态保持、结构化页面观察。
- 不要和 CLI 混在同一个实验里。先做单变量比较。

### 5. ChromeDevTools/chrome-devtools-mcp

一句话：这是 Chrome DevTools 的 MCP 化，不是跨浏览器自动化框架。

核心设计：

- MCP server 暴露 Chrome DevTools / Puppeteer 能力。
- 工具覆盖 input、navigation、emulation、performance、network、debugging、memory、extensions、third-party/WebMCP。
- 特别强调 performance trace、Lighthouse、console、network、source-mapped stack traces。

好品味：

- 目标明确：调试和性能，不假装自己是所有浏览器自动化的统一答案。
- design principles 里强调 token-optimized、small deterministic blocks、large assets 返回路径/URI 而不是塞上下文。这是正确方向。

风险：

- Chrome-only。官方支持 Google Chrome 和 Chrome for Testing，其他 Chromium 不保证。
- telemetry 默认开启，可用 `--no-usage-statistics` 或环境变量关闭。
- performance tools 可能调用 CrUX 相关数据；对隐私/合规敏感的环境要显式关。
- 连接本机 Chrome remote debugging port 时，本地其他进程也可能控制浏览器。这个风险不是文档问题，是 CDP 的本质。

适合本仓库学习：

- 用于调研“Agent 如何做 Web 性能/调试诊断”。
- 不要拿它替代 Playwright 做跨浏览器 E2E。

### 6. vercel-labs/agent-browser

一句话：一个面向 Agent 的完整浏览器 CLI，Rust 原生，功能面很宽。

核心设计：

- CLI-first，支持 `open`、`snapshot`、`click`、`fill`、`find role/text/label`、wait、batch、network、cookies/storage、tabs、frames、dialogs、diff、debug、React/Web Vitals。
- 支持 Chrome profile reuse、persistent profile、session persistence、state file、auth vault。
- 安全能力包括 content boundaries、domain allowlist、action policy、action confirmation、max output。
- 有 dashboard 和 AI chat 能力。

好品味：

- 认真处理了几个 Agent 浏览器工具常见烂点：页面内容 prompt injection、域名外泄、危险动作确认、输出过大。
- `batch` 命令对 CLI 场景很实际，可以减少进程启动开销。
- auth vault 设计比“把密码丢给 LLM”好得多。

风险：

- README 明确：安全功能是 opt-in，默认不限制导航、动作、输出。默认 unrestricted 不能直接用于敏感场景。
- 功能太多，概念也多：session、session-name、profile、state、auth vault、provider、dashboard、AI chat。能力强，但抽象面也宽。
- open issues 很多，不能只看 star 数判断成熟度。

适合本仓库学习：

- 适合研究“面向 Agent 的 CLI 应该怎么设计安全边界”。
- 也适合作为 Playwright CLI 的对照组：同样是 CLI-first，但一个贴 Playwright，一个自成体系。

### 7. epiral/bb-browser

一句话：它的核心不是“浏览器自动化”，而是“把真实浏览器登录态变成 Agent 可用 API”。

核心设计：

- CLI + MCP server + local daemon + Chrome extension。
- 默认链路：Agent -> CLI/MCP -> localhost daemon -> Chrome extension / CDP -> 用户真实浏览器。
- 通过 `site` adapter 把网站变成命令行 API；README 声称 36 平台、103 命令，社区 adapter 在 `epiral/bb-sites`。
- 支持 `eval`、带 cookie 的 `fetch()`、页面内部模块调用、network capture、tab 管理、截图。

好品味：

- 直接承认现实：大多数网站没有好 API，用户却已经在浏览器里登录了。
- site adapter 是比“LLM 每次重新读页面再猜按钮”更可控的中间层。
- privacy 文档说通信本地化、无 telemetry、无外部服务器、数据只在内存中处理。这个边界写得清楚。

风险：

- 它复用真实登录态，所以能力边界就是用户账号边界。强大，也危险。
- adapter 会依赖站点 DOM、接口、webpack 模块、CSRF 逻辑；站点一改就会坏。
- “网站以为是你，因为就是你”这句话在工程上很实用，在安全上也很刺眼。必须用 dedicated profile、低权限账号、只读任务和人工审批。
- 不适合无状态 CI 或严肃 E2E 测试。它是资料获取和站点能力封装，不是测试框架基座。

适合本仓库学习：

- 非常适合研究“Agent 如何访问登录后互联网”和“CLI adapter 是否比 MCP 工具更适合 Agent”。
- 高风险动作必须人工审查。这个仓库的 AGENTS 规则已经写了：发邮件、改数据库、支付、执行 shell、写文件都要有人审。

### 8. browser-use/browser-use

一句话：这是浏览器 Agent 框架，不是简单 CLI。

核心设计：

- Python package，核心用法是 `Agent(task=..., llm=..., browser=...)`。
- 支持 `ChatBrowserUse`、Google、Anthropic 等 LLM provider。
- 有 open-source agent，也有 Browser Use Cloud。
- CLI 可做 persistent browser automation：`open`、`state`、`click`、`type`、`screenshot`。
- README 把 form filling、shopping、personal assistant 作为典型任务。

好品味：

- 把“任务 -> LLM -> 浏览器动作 -> 状态反馈”的循环包装起来，适合快速验证 autonomous web agent。
- 有 benchmark 意识，至少知道不能只靠 demo 说话。
- Python 接入容易，适合 fieldbook 的实验记录。

风险：

- 依赖面很重，框架边界大。它一旦进入核心链路，调试成本会高于 Playwright/CLI。
- LLM 决策循环天然不确定。要做生产任务，必须加 domain allowlist、action approval、evals、trace、失败回放。
- 默认 anonymized telemetry 为 true，源码里用 PostHog；可通过 `ANONYMIZED_TELEMETRY=False` 关闭。
- Cloud 方案有 stealth、proxy、captcha、filesystem/memory 等能力，但这已经从“开源浏览器自动化”进入“托管 Agent 产品”范畴，合规和成本要单独评估。

适合本仓库学习：

- 适合研究“高级 Agent 框架如何组织浏览器任务”。
- 不适合当第一个 lab。先用 Playwright/CLI/MCP 搞清楚状态、工具调用、观测和失败处理，再看它。

## 横向维度分析

### 1. 页面观察：别迷信截图

主流路径有四种：

| 观察方式 | 代表工具 | 优点 | 风险 |
|---|---|---|---|
| Accessibility snapshot | Playwright MCP、Playwright CLI、agent-browser、bb-browser | 结构化、可引用 ref、比截图省 token | 页面可访问性差时信息不完整 |
| DevTools / CDP 数据 | chrome-devtools-mcp、bb-browser、agent-browser | network、console、performance、memory 更强 | Chrome/CDP 绑定更强 |
| 视觉截图 | Playwright、agent-browser、chrome-devtools-mcp | UI 审查、布局、视觉回归需要 | 给 LLM 看图成本高且不确定 |
| 站点 adapter | bb-browser | 输出结构化 JSON，最省上下文 | 维护 adapter 成本，站点变更会破坏 |

好方案不是“全都用”。好方案是按任务选择最小观察面：

- 表单/点击：snapshot + refs。
- 性能诊断：DevTools trace。
- UI 审查：screenshot + DOM/box。
- 登录后资料收集：adapter 或 authenticated fetch。

### 2. 状态与认证：这是浏览器自动化最容易烂的地方

状态模型对比：

| 模型 | 代表工具 | 工程含义 |
|---|---|---|
| 隔离 context / storage state | Playwright、Playwright Python、Playwright MCP | 可复现、适合测试 |
| persistent profile | Playwright CLI、Playwright MCP、agent-browser | 本地连续任务方便，但要管并发和清理 |
| 复制真实 Chrome profile | agent-browser、browser-use 部分模式 | 省登录步骤，但敏感 |
| 真实浏览器登录态直接复用 | bb-browser | 最接近用户真实互联网，但风险最大 |
| LLM/Cloud 管理浏览器状态 | browser-use cloud | 能力强，但合规、成本、可审计性另算 |

原则：

- 测试用隔离 context。
- 研究用 dedicated profile。
- 不要把个人默认 Chrome profile 交给 Agent 做高风险任务。
- 任何能读 cookie/session/page content 的工具，都不是“安全小工具”。

### 3. CLI vs MCP：别搞宗教战争

CLI 更适合：

- coding agent 在代码仓库里跑测试、截图、抓 trace。
- 命令短、输出可落文件、上下文预算紧。
- 人可以读命令日志，复现容易。

MCP 更适合：

- 工具发现、长会话、持续状态。
- MCP 客户端生态统一接入。
- Agent 需要 rich introspection，而不是每次 shell 调命令。

结论：

- 对本仓库早期实验，CLI 和 MCP 都要研究，但不要一上来混用。
- 同一任务分别用 `playwright-cli` 和 `playwright-mcp` 跑，比较 token、动作数、失败恢复和调试成本。这才是有用实验。

### 4. 安全：默认安全才算安全，opt-in 只能算工具箱

安全维度对比：

| 项目 | 明确安全/隐私机制 | 主要风险 |
|---|---|---|
| Playwright | isolation context、storage state、trace 可审计 | 代码使用者自己负责边界 |
| Playwright MCP | allowed/block origins、file access、isolated、storage state、secrets 等配置；声明不是安全边界 | MCP client 可见页面数据；profile 并发冲突 |
| Chrome DevTools MCP | opt-out telemetry、isolated profile、browser-url、auto-connect 等 | 默认 telemetry；CDP/remote debugging 风险；Chrome-only |
| agent-browser | auth vault、content boundaries、domain allowlist、action policy、confirmation、max output | 全部 opt-in，默认 unrestricted |
| bb-browser | privacy 文档声明本地通信、无 telemetry、无外部服务器 | 真实登录态暴露给 Agent 能力边界；adapter 可执行页面内逻辑 |
| browser-use | allowed domains 测试、telemetry 可关、cloud 与自托管模式 | 默认 telemetry；LLM 决策不可完全确定；cloud 合规另算 |

实用规则：

- Agent 浏览器任务必须先设 domain allowlist。
- 页面内容进入 LLM 前要做边界标记或显式 provenance。
- `eval`、download、upload、payment、send message、submit form 这类动作默认要人工确认。
- 不要把“工具本地运行”误解成“数据安全”。本地 LLM/Agent 也会读到页面内容。

### 5. 维护成熟度：看层级，不只看 star

成熟度判断：

- Playwright 主仓库最成熟，是事实标准级别。
- Playwright Python 是成熟绑定，适合 Python 生态。
- browser-use star 很高、增长快，但它是更大的 Agent 框架，复杂度也高。
- Chrome DevTools MCP、Playwright MCP、Playwright CLI 都是官方/大厂背景的新 Agent 接口层，更新很快，但 API 稳定性要谨慎。
- agent-browser 功能推进很快，安全功能做得认真，但 open issues 高，实际采用前要跑自己的任务集。
- bb-browser 方向实用，适合中文互联网/登录态研究，但 adapter 生态和真实站点变化是长期维护成本。

## 给本仓库的建议

### 推荐学习顺序

1. Playwright / Playwright Python：先掌握浏览器自动化的基本数据结构。
2. Playwright CLI：研究 coding agent 如何低成本驱动浏览器。
3. Playwright MCP：研究 MCP browser tool 的标准形态。
4. Chrome DevTools MCP：研究性能、console、network、memory 诊断。
5. agent-browser：研究 CLI-first 工具如何设计 auth/session/security。
6. bb-browser：研究登录态互联网访问和 site adapter。
7. browser-use：最后研究完整 browser agent 框架。

这个顺序不是保守，是为了避免一开始就把 LLM 决策、浏览器状态、MCP、登录态、站点适配器全混在一起。那样调不出结论，只会得到一堆噪音。

### 最小实验路线

实验 1：Playwright 基线

- 目标：理解 `BrowserContext`、locator、storage state、trace。
- 工具：`microsoft/playwright-python` 或 `microsoft/playwright`。
- 验收：同一任务重复 5 次，行为一致；失败时能用 trace 复盘。

实验 2：CLI vs MCP 对照

- 目标：比较 `playwright-cli` 和 `playwright-mcp` 在同一网页任务上的成本。
- 指标：动作数、token/上下文占用、失败恢复、截图/trace 产物、人类接管便利性。
- 注意：同一个任务不要同时用两个工具；分开跑。

实验 3：DevTools 诊断

- 目标：让 Agent 找出一个页面的 console error、慢请求、LCP/trace 问题。
- 工具：`chrome-devtools-mcp`。
- 验收：输出问题、证据、复现步骤，不只给泛泛优化建议。

实验 4：登录态资料获取

- 目标：用 dedicated Chrome profile 做只读资料获取。
- 工具：`bb-browser` 或 `agent-browser`。
- 约束：低权限账号、domain allowlist、禁止 destructive action、人工确认。

实验 5：Browser Agent 框架

- 目标：评估 `browser-use` 在开放任务上的成功率和失败模式。
- 指标：成功率、平均动作数、人工介入次数、错误类型、是否泄露或越界。
- 约束：必须有 evals，不能靠一次 demo 下结论。

## 采用决策

如果现在要在本仓库选工具：

- 底座：选 Playwright。没有争议。
- Python lab：选 Playwright Python。
- coding agent 浏览器测试：优先试 Playwright CLI。
- MCP 浏览器实验：优先试 Playwright MCP。
- 性能/调试专项：用 Chrome DevTools MCP。
- 真实登录态站点研究：谨慎试 bb-browser，必须 dedicated profile。
- 安全策略和 CLI 设计研究：重点拆 agent-browser。
- 高层 autonomous web task：用 browser-use 做研究对象，不要直接当生产依赖。

不要做的事：

- 不要自己写一个浏览器自动化内核。
- 不要让 Agent 直接操控个人默认 Chrome profile。
- 不要把 `browser-use`、`playwright-mcp`、`agent-browser`、`bb-browser` 混在一个实验里，然后说“效果不好”。那是实验设计烂。
- 不要只看 stars。真实指标是：状态边界清不清楚、失败能不能复盘、安全默认值是否保守、输出是否可审计。

## 来源

GitHub 仓库：

- bb-browser: https://github.com/epiral/bb-browser
- bb-sites: https://github.com/epiral/bb-sites
- browser-use: https://github.com/browser-use/browser-use
- Playwright CLI: https://github.com/microsoft/playwright-cli
- Chrome DevTools MCP: https://github.com/ChromeDevTools/chrome-devtools-mcp
- agent-browser: https://github.com/vercel-labs/agent-browser
- Playwright: https://github.com/microsoft/playwright
- Playwright MCP: https://github.com/microsoft/playwright-mcp
- Playwright Python: https://github.com/microsoft/playwright-python

包与发布：

- npm `bb-browser`: https://www.npmjs.com/package/bb-browser
- npm `@playwright/cli`: https://www.npmjs.com/package/@playwright/cli
- npm `chrome-devtools-mcp`: https://www.npmjs.com/package/chrome-devtools-mcp
- npm `agent-browser`: https://www.npmjs.com/package/agent-browser
- npm `playwright`: https://www.npmjs.com/package/playwright
- npm `@playwright/mcp`: https://www.npmjs.com/package/@playwright/mcp
- PyPI `browser-use`: https://pypi.org/project/browser-use/
- PyPI `playwright`: https://pypi.org/project/playwright/

关键文档：

- Playwright docs: https://playwright.dev/
- Playwright Python docs: https://playwright.dev/python/
- Chrome DevTools MCP tool reference: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md
- Chrome DevTools MCP design principles: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/design-principles.md
- agent-browser security: https://agent-browser.dev/security
- browser-use docs: https://docs.browser-use.com/
