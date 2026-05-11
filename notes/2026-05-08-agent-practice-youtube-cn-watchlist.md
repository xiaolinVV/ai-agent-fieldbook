# 中文 AI Agent 实践落地 YouTube 学习清单

日期：2026-05-08

补充日期：2026-05-09，补充 RAGFlow 相关中文视频与开源项目线索。

## 今天筛了什么

本次筛选目标不是继续找 SDK / API 教学，而是找中文 YouTube 上和 AI Agent 实际应用相关的内容：

- 基于 Agent 技术的实际应用场景
- 开源项目、源码解读、项目拆解
- 企业级落地、可观测性、评估、延迟、质量控制
- Dify / n8n / Coze / RAGFlow / LangGraph / RAG / Agentic RAG 等实践路线
- 值得持续关注的中文频道

检索关键词：

- `AI Agent 企业落地 中文 案例`
- `AI Agent 应用场景 实战 中文`
- `AI Agent 开源项目 中文 LangGraph AutoGen Dify`
- `Dify AI Agent 企业落地 中文 实战`
- `n8n AI Agent 自动化 实战 中文 企业`
- `LangGraph 中文 实战 项目 Agent 企业级`
- `AI Agent 开源项目 源码 解读 中文`
- `AI Agent 大厂 落地 可观测性 延迟 中文`
- `AI Agent RAG 企业知识库 中文 实战`
- `AI Agent 客服 销售 自动化 中文 实战`
- `AutoGen CrewAI AI Agent 中文 实战 项目`
- `RAGFlow 中文 教程 企业知识库`
- `RAGFlow Dify 对比 中文 RAG`
- `RAGFlow 源码 解读 中文 RAG`

## 核心判断

中文 YouTube 里，真正贴近落地的内容不多。大部分视频有三个问题：

- 讲“自动赚钱”“AI 员工”“一人公司”，但不讲业务闭环。
- 展示工具点击流程，但不讲权限、评估、失败处理、数据安全。
- 讲多 Agent 很热闹，但没有解释为什么单 Agent 或 workflow 不够。

值得优先看的内容有几个特征：

- 明确业务对象：客服、销售、知识库、数据查询、研究报告、DevOps、内容生产。
- 明确工程边界：RAG、工具调用、工作流、日志、评估、可观测性、延迟。
- 能和开源项目或可复现实验对应起来，而不是只展示商业工具界面。

RAGFlow 要单独看。它和 Dify、n8n、Coze 不是完全同类：Dify/n8n/Coze 更偏应用编排和工作流，RAGFlow 更偏 RAG 引擎、文档解析、切分、召回、引用和知识库质量。把它们混成一个“AI 工具”篮子，是坏味道。

## 第一优先级

已沉淀：

- [RAG 工作机制详解——一个高质量知识库背后的技术全流程](RAG%20工作机制详解——一个高质量知识库背后的技术全流程.md)

| 顺序 | 视频 | 频道 | 适合学什么 | 判断 |
|---|---|---|---|---|
| 1 | [【人工智能】LangChain 年度报告 \| Agent 现状 \| 大厂如何落地 \| 输出质量 \| 延迟痛点 \| 多模型 \| 可观测性 \| 2025 趋势](https://www.youtube.com/watch?v=KcC1JCiHMk8) | 最佳拍档 | 企业落地真实约束、质量、延迟、可观测性 | 必看。比“Agent 能做什么”更重要的是“为什么落地难”。 |
| 2 | [工业级实战：从传统 RAG 到 Agentic RAG 的进阶优化](https://www.youtube.com/watch?v=UZs_yOKcw7A) | 白白说大模型 | 企业知识库、Agentic RAG、检索增强落地 | 实践价值高，适合从知识库场景切入 Agent。 |
| 3 | [RAG 工作机制详解：一个高质量知识库背后的技术全流程](https://www.youtube.com/watch?v=WWdlme1EAGI) | 马克的技术工作坊 | 企业知识库基础、RAG 质量链路 | 虽然不是纯 Agent，但这是企业 Agent 最常见底座。 |
| 4 | [Agent Skills 做知识库检索，能比传统 RAG 效果更好吗？](https://www.youtube.com/watch?v=YL-BgiruIe0) | code 秘密花园 | Skills 与 RAG 的边界、知识检索新模式 | 适合比较传统 RAG 和 Agent/Skills 路线。 |
| 5 | [还在自己拼装 RAG 系统？Onyx 整合 Agentic RAG，打造企业级 AI 知识库](https://www.youtube.com/watch?v=_ndl8_bTF2I) | GitCovery | Onyx、开源企业知识库、Agentic RAG | 开源项目落地方向，值得跟官方 repo 一起看。 |
| 6 | [RAGFlow：知识库终极引擎](https://www.youtube.com/watch?v=9x-9-r2ifig) | huangyihe | RAGFlow、知识库引擎、企业 RAG | RAGFlow 中文优先入口，后续要对照官方文档复核版本。 |
| 7 | [RAGFlow：采用 OCR 和深度文档理解的新一代 RAG 引擎](https://www.youtube.com/watch?v=Z5AV6d1He4k) | AIGCLINK | 深度文档理解、引用来源、异构数据源 | 适合建立 RAGFlow 特性地图，但发布时间较早。 |
| 8 | [Dify + RAGFlow：1 + 1＞2 的混合架构，详细教程 + 实施案例](https://www.youtube.com/watch?v=r3PxNVadt3c) | Willwei | Dify 编排 + RAGFlow 知识库 | 适合理解职责分离：Dify 管流程，RAGFlow 管知识库质量。 |
| 9 | [LangChain Deep Agents：构建你自己的深度研究智能体](https://www.youtube.com/watch?v=FXE6W1Snl3g) | 01Coder | Deep Research / 研究型 Agent | 适合作为“调研报告 Agent”的实践样板。 |
| 10 | [【喂饭教程】Dify + Agent 快速搭建数据查询 AI 应用](https://www.youtube.com/watch?v=ULK9tlyZPqY) | 大模型 | Dify、自然语言查数据、多数据源切换 | 业务场景明确，比泛泛工具演示更值得看。 |
| 11 | [Dify + Tavily 构建 DeepResearch Agent：企业级自动化调研系统全流程实战](https://www.youtube.com/watch?v=ERR4DaNoaHY) | 木研 muyan | 自动化调研、搜索、引用溯源、报告生成 | 播放量低，但题目方向对，适合后续验证。 |
| 12 | [超详细教学：n8n AI 实作 0 基础入门到进阶](https://www.youtube.com/watch?v=vvqhzbp4J5A) | HC AI 说人话 | n8n、RAG、Webhook、自动研究报告 | 工作流自动化方向的中文大课。 |
| 13 | [AI Agent 终极教学：35 分钟从概念到 n8n 实战](https://www.youtube.com/watch?v=lVVSY59EcYE) | Automate with Bonnie | n8n 实战、业务自动化入门 | 可以作为 n8n Agent 路线的快速入口。 |

## 企业落地与工程化观察

这组不要当成代码教程看，要看“落地为什么难”。

| 视频 | 频道 | 看点 |
|---|---|---|
| [LangChain 年度报告：Agent 现状、大厂如何落地、输出质量、延迟痛点、可观测性](https://www.youtube.com/watch?v=KcC1JCiHMk8) | 最佳拍档 | 企业落地最关键的不是多 Agent，而是稳定性、可观测性、评估和成本延迟。 |
| [AI Agent 的主流设计模式：从单 Agent 到多 Agent，从自有决策到工程化落地](https://www.youtube.com/watch?v=PANR5MPHosY) | 白白说大模型 | 适合看 Agent 设计模式，不要一开始就多 Agent。 |
| [从 Claude 小卖部实验破产看 AI 落地真相：AI Agent 的未来](https://www.youtube.com/watch?v=vd1XoGasyXw) | 白白说大模型 | 看失败案例比看成功故事更有用，重点关注边界条件。 |
| [AI Agent 的进化：从单次 API 调用到稳定多智能体协同](https://www.youtube.com/watch?v=L8KnIv8ZU04) | 白白说大模型 | 适合理解从 API 调用到 Agent 系统的演进。 |
| [E231：从 B2B 到 A2A：Agent 新基建，如何让“一人企业”做全球生意？](https://www.youtube.com/watch?v=B6eAjzDVhr8) | 硅谷 101 播客 | 偏商业/产业视角。可看趋势，不当工程指南。 |

## 开源项目与源码拆解

这组适合放到 `research/open-source-projects/` 后续深挖。先看视频判断项目是否值得拆，再回到 GitHub 看源码，不要只听讲解。

| 视频 | 频道 | 项目/方向 | 判断 |
|---|---|---|---|
| [还在自己拼装 RAG 系统？Onyx 整合 Agentic RAG，打造企业级 AI 知识库](https://www.youtube.com/watch?v=_ndl8_bTF2I) | GitCovery | Onyx / 企业搜索 / Agentic RAG | 值得作为企业知识库开源项目候选。 |
| [RAGFlow：知识库终极引擎](https://www.youtube.com/watch?v=9x-9-r2ifig) | huangyihe | RAGFlow / RAG 引擎 / 企业知识库 | 值得作为企业 RAG 引擎候选，重点看文档解析、切分、召回、引用和评估。 |
| [AI 专用浏览器 Agent Browser 开源代码深度解析](https://www.youtube.com/watch?v=J2oRlhbQKUk) | Koala 聊开源 | browser agent / 浏览器自动化 | 适合研究浏览器 Agent 的边界和风险。 |
| [agent-browser：让 AI 接管浏览器｜比 MCP 省 Token｜详解 + 实测](https://www.youtube.com/watch?v=YZIh0mTQ9rE) | NiceKate AI | 浏览器 Agent | 可看实测，但要警惕只看效果、不看权限控制。 |
| [开源项目 Chaterm，运维版 “Cursor”，让 AI Agent 帮你轻松管理服务器](https://www.youtube.com/watch?v=pZmMyu4qaHg) | 三少科技 | DevOps / terminal agent | 高风险场景，重点看权限、人审、审计。 |
| [完全开源可控的语音 AI Agent 技术栈](https://www.youtube.com/watch?v=wLcDSl-PQRE) | WasmEdge 中文 | 语音 Agent 技术栈 | 适合语音入口、边缘部署、本地化方向。 |
| [OpenClaw 开源生态全景解读：14 个 AI Agent 项目，从 56 万行到 888KB](https://www.youtube.com/watch?v=qWfYa5m4wHM) | 唐国梁 Tommy | OpenClaw 生态 | 先列为候选，后续必须核实官方 repo、安全性和维护状态。 |
| [OpenClaw 多智能体机制：编排你的 Agents 团队](https://www.youtube.com/watch?v=UztyaJ_EKKM) | 01Coder | 多 Agent 编排 | 可看机制，不要直接照搬多 Agent 架构。 |
| [【源码解析】Agentic RAG 智能问答系统 Agent 项目实现思路及核心源码讲解](https://www.youtube.com/watch?v=TUP3Qrq0XKk) | 唐国梁 Tommy | Agentic RAG / 源码解析 | 播放量不高，但题目和源码方向对。 |

## RAGFlow / 企业 RAG 专项

RAGFlow 官方仓库把自己定位为开源 RAG 引擎，并强调 Agent 能力、深度文档理解、引用溯源、异构数据源和自动化 RAG workflow。学习它时别只看“本地部署成功”，真正要看文档质量链路：解析、切分、索引、召回、重排、引用、人审和评估。

| 视频 | 频道 | 适合学什么 | 判断 |
|---|---|---|---|
| [RAGFlow：知识库终极引擎](https://www.youtube.com/watch?v=9x-9-r2ifig) | huangyihe | RAGFlow 全局理解、知识库引擎定位 | 中文优先入口。看完要回官方 repo/docs 校准。 |
| [RAGFlow：采用 OCR 和深度文档理解的新一代 RAG 引擎](https://www.youtube.com/watch?v=Z5AV6d1He4k) | AIGCLINK | 深度文档理解、引用来源、异构数据源、降低幻觉 | 适合看项目能力地图，发布时间较早，API/版本可能过时。 |
| [RAGFlow 命中率最高的 RAG 知识库引擎 本地部署 小白教程](https://www.youtube.com/watch?v=bCPHt6HxbP8) | augustdoit | 本地部署、知识库创建 | 入门部署可看，但不要把“跑起来”当落地完成。 |
| [Ragflow 小白教程（详细重制版）](https://www.youtube.com/watch?v=zpZKOSv4nIQ) | augustdoit | 本地部署重制教程 | 可作为部署补充，优先核对最新 Docker / compose 文档。 |
| [零基础教程：RAGFlow 快速创建知识库和智能问答系统](https://www.youtube.com/watch?v=bBaRtI9yUKE) | 科技标签 Appmark | 知识库、智能问答系统快速搭建 | 适合产品级上手，不足是工程边界可能讲得少。 |
| [Dify + RAGFlow：1 + 1＞2 的混合架构，详细教程 + 实施案例](https://www.youtube.com/watch?v=r3PxNVadt3c) | Willwei | Dify + RAGFlow 混合架构 | 很值得看，重点理解“应用编排”和“知识检索”不要混在一起。 |
| [RAGFlow 作为外部知识库接入 Dify](https://www.youtube.com/watch?v=gaDuU9Oq1H4) | 点击投喂卓师傅 | RAGFlow 外部知识库、Dify 集成 | 播放量不高，但题目直击集成边界。 |
| [Qwen3 + RAGFlow 构建个人知识库](https://www.youtube.com/watch?v=55C2TqlSt1Y) | AI 大模型小冉 Agent | Qwen + RAGFlow、本地知识库 | 可看模型接入和流程，标题夸张，按步骤验证。 |
| [DeepSeek + RAGFlow 构建个人知识库，2026 本地化部署](https://www.youtube.com/watch?v=f_vA0C1gBII) | AI 大模型小冉 Agent | DeepSeek + RAGFlow、本地部署 | 新一些，但仍需核实版本和依赖。 |
| [RAGflow 知识库 + 参数可调架构 + 本地大模型，让 AI 化身佛学顾问](https://www.youtube.com/watch?v=8la6SQFJVhY) | 代码修理工 | 垂直知识库案例、本地模型 | 场景窄，适合看参数调优和领域语料处理。 |
| [用 RAGFlow 打造 AI 医疗问诊助手](https://www.youtube.com/watch?v=-LWFrIoQ5V4) | AI 大模型小冉 Agent | 医疗问诊知识库案例 | 高风险场景，只看技术流程，不能当真实医疗落地范式。 |

## Dify / n8n / No-Code 工作流

这类视频容易变成工具营销。只看能落到业务流、数据源、权限、回滚和人工确认的内容。

| 视频 | 频道 | 适合场景 | 判断 |
|---|---|---|---|
| [Dify + Agent 快速搭建数据查询 AI 应用](https://www.youtube.com/watch?v=ULK9tlyZPqY) | 大模型 | 企业数据查询、自然语言查数 | 场景明确，优先看。 |
| [Dify + Tavily 构建 DeepResearch Agent](https://www.youtube.com/watch?v=ERR4DaNoaHY) | 木研 muyan | 自动调研、报告生成、引用溯源 | 适合研究型 Agent。 |
| [Dify 零基础教程：Workflow 与 Chatflow 模式详解 + 节点配置实战](https://www.youtube.com/watch?v=ZKmVvtSAEek) | 白小菌 | Dify 工作流基础 | 入门可看，但要补企业权限和测试。 |
| [0 代码开发工业级 Agent，Dify 快速入门与开发实战](https://www.youtube.com/watch?v=d0HQ9Y4_LmQ) | 赋范课堂 | Dify 多场景应用 | 标题很满，筛着看具体案例。 |
| [n8n AI 实作 0 基础入门到进阶](https://www.youtube.com/watch?v=vvqhzbp4J5A) | HC AI 说人话 | n8n、Webhook、RAG、研究报告 | n8n 路线优先入口。 |
| [最强开源 AI 工作流 n8n，上千插件 + 模板，效率起飞](https://www.youtube.com/watch?v=cVPD2AFlLIs) | 技术爬爬虾 TechShrimp | n8n 产品能力、生态 | 适合了解工具，不当架构指南。 |
| [n8n AI Agent 终极教学：从概念到实战](https://www.youtube.com/watch?v=lVVSY59EcYE) | Automate with Bonnie | n8n Agent 实战 | 快速建立手感。 |
| [n8n + AI + 飞书，把短视频生产和小红书自动发布变成按时打卡](https://www.youtube.com/watch?v=Sj133Lm320E) | 南哥 AGI 研习社 | 内容生产自动化 | 可看业务流，但发布动作属于高风险，需要人审。 |

## LangGraph / LangChain / 多 Agent 框架实践

这组适合后续从 `labs/` 里做实验复现。

| 视频 | 频道 | 适合学什么 | 判断 |
|---|---|---|---|
| [LangChain Deep Agents：构建你自己的深度研究智能体](https://www.youtube.com/watch?v=FXE6W1Snl3g) | 01Coder | Deep Research Agent | 推荐。研究型 Agent 是真实场景。 |
| [LangGraph 全解：AI Agent 核心框架实战指南，构建企业级智能体](https://www.youtube.com/watch?v=iEk8GVxa34A) | AI 大模型教程 | LangGraph 企业级智能体 | 候选。需核实源码和版本是否过时。 |
| [手搓企业级 Agent：借助 LangGraph 构建智能数据分析助手](https://www.youtube.com/watch?v=xD7btIPI-Ew) | 赋范课堂 | 数据分析 Agent | 候选。标题很满，重点看是否有可运行代码。 |
| [最新 LangChain 1.0 快速入门与 Agent 开发实战](https://www.youtube.com/watch?v=PEI7lhcrlQU) | 赋范课堂 | LangChain 1.0 / Agent API / Deep Agents | 可看新 API，但必须对照官方文档。 |
| [基于 LangChain 和 LangGraph 实现 Agent 分诊工作流](https://www.youtube.com/watch?v=iPGBgSdZCFY) | AI 大模型小冉 Agent | 动态路由、短长期记忆、RAG | 场景明确，适合拆工作流。 |
| [基于 LangChain 和 LangGraph 框架实现 Agent 分诊工作流](https://www.youtube.com/watch?v=63wwAy99j54) | 南哥 AGI 研习社 | 分诊工作流、工具调用、RAG | 同类候选，后续择优看。 |
| [CrewAI + FastAPI 打造多 Agent 协作应用并对外提供 API 服务](https://www.youtube.com/watch?v=2TE5DlYlvGw) | 南哥 AGI 研习社 | 多 Agent 服务化 | 适合看怎么把 Agent 暴露成 API。 |
| [AutoGen 实战，打造自己的 AI Agent 如此的简单靠谱](https://www.youtube.com/watch?v=ygGMycX2IBE) | 洛克船长 | AutoGen 入门实战 | 较旧，作为历史路线了解。 |

## 业务应用场景

| 场景 | 视频 | 频道 | 风险提示 |
|---|---|---|---|
| 客服/销售电话 | [GPT 也接打电话？AI 完全取代销售、客服、预约、代打的 AI Agent](https://www.youtube.com/watch?v=C3f9LSELYjI) | Automate with Bonnie | 涉及电话外呼，真实落地要处理合规、录音、用户授权。 |
| 潜客回复 | [我用 n8n 打造业务 AI Agents，3 分钟内专业回复潜在客户](https://www.youtube.com/shorts/MxtbZ4Mmk14) | 刘彦廷 | Shorts 只能看思路，不能当完整教程。 |
| 新闻/公众号自动化 | [AI Agent 实战：用 Claude 打通新闻自动化 & 微信公众号发布](https://www.youtube.com/watch?v=h19uVMsB2_g) | 圆桌辣妈派 | 自动发布是高风险动作，必须有人审。 |
| 研究报告 | [Dify + Tavily 构建 DeepResearch Agent](https://www.youtube.com/watch?v=ERR4DaNoaHY) | 木研 muyan | 重点看引用溯源和报告质量。 |
| 企业知识库 | [Onyx 整合 Agentic RAG，打造企业级 AI 知识库](https://www.youtube.com/watch?v=_ndl8_bTF2I) | GitCovery | 重点看权限、数据隔离、检索评估。 |
| 企业 RAG 引擎 | [RAGFlow：知识库终极引擎](https://www.youtube.com/watch?v=9x-9-r2ifig) | huangyihe | 重点看文档解析、召回、引用和 RAG 质量评估。 |
| Dify + RAGFlow 混合架构 | [Dify + RAGFlow：1 + 1＞2 的混合架构](https://www.youtube.com/watch?v=r3PxNVadt3c) | Willwei | 适合理解 Dify 负责编排、RAGFlow 负责知识库质量的分工。 |
| 数据查询 | [Dify + Agent 快速搭建数据查询 AI 应用](https://www.youtube.com/watch?v=ULK9tlyZPqY) | 大模型 | 查询可以自动，写库必须人审。 |
| DevOps 运维 | [开源项目 Chaterm，运维版 Cursor](https://www.youtube.com/watch?v=pZmMyu4qaHg) | 三少科技 | Shell / 服务器操作是高风险，必须审计和人工确认。 |

## 值得关注的频道

| 频道 | 推荐级别 | 适合跟踪什么 |
|---|---:|---|
| [白白说大模型](https://www.youtube.com/results?search_query=%E7%99%BD%E7%99%BD%E8%AF%B4%E5%A4%A7%E6%A8%A1%E5%9E%8B+AI+Agent+%E8%90%BD%E5%9C%B0) | S | Agent 落地、设计模式、Agentic RAG、失败案例。 |
| [马克的技术工作坊](https://www.youtube.com/results?search_query=%E9%A9%AC%E5%85%8B%E7%9A%84%E6%8A%80%E6%9C%AF%E5%B7%A5%E4%BD%9C%E5%9D%8A+RAG+Agent) | S | RAG、Agent 原理、工程拆解。 |
| [huangyihe](https://www.youtube.com/results?search_query=huangyihe+RAGFlow+RAG) | A | RAGFlow、Dify、Claude Code、Agent 工作流，适合作为中文技术入口。 |
| [01Coder](https://www.youtube.com/results?search_query=01Coder+Agent+LangChain+OpenClaw) | A | 开源 Agent、Deep Agents、Claude Skills、工程实操。 |
| [最佳拍档](https://www.youtube.com/results?search_query=%E6%9C%80%E4%BD%B3%E6%8B%8D%E6%A1%A3+LangChain+Agent+%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A) | A | 报告解读、技术趋势、工程约束。 |
| [GitCovery](https://www.youtube.com/results?search_query=GitCovery+Agentic+RAG+Onyx) | A- | 开源项目发现，尤其是企业知识库、Agentic RAG。 |
| [AIGCLINK](https://www.youtube.com/results?search_query=AIGCLINK+RAGFlow+Agent) | B+ | RAGFlow、CrewAI、AutoGen 等开源 Agent/RAG 项目介绍。 |
| [HC AI 说人话](https://www.youtube.com/results?search_query=HC+AI+%E8%AF%B4%E4%BA%BA%E8%AF%9D+n8n+Agent) | B+ | n8n、自动化工作流。 |
| [技术爬爬虾 TechShrimp](https://www.youtube.com/results?search_query=%E6%8A%80%E6%9C%AF%E7%88%AC%E7%88%AC%E8%99%BE+n8n+RAG+Agent) | B+ | 工具生态、RAG、n8n 入门。 |
| [赋范课堂](https://www.youtube.com/results?search_query=%E8%B5%8B%E8%8C%83%E8%AF%BE%E5%A0%82+LangGraph+Agent) | B | LangGraph/LangChain 长课很多，但标题常过满，挑有源码的看。 |
| [南哥 AGI 研习社](https://www.youtube.com/results?search_query=%E5%8D%97%E5%93%A5+AGI+%E7%A0%94%E4%B9%A0%E7%A4%BE+Agent) | B | CrewAI、LangGraph、n8n、场景案例。 |
| [Automate with Bonnie](https://www.youtube.com/results?search_query=Automate+with+Bonnie+n8n+AI+Agent+%E4%B8%AD%E6%96%87) | B | n8n、业务自动化、客服销售场景。 |
| [唐国梁 Tommy](https://www.youtube.com/results?search_query=%E5%94%90%E5%9B%BD%E6%A2%81+Agent+%E6%BA%90%E7%A0%81+%E5%BC%80%E6%BA%90) | B | 框架横评、源码解析、开源生态。需自行过滤标题党。 |
| [NiceKate AI](https://www.youtube.com/results?search_query=NiceKate+AI+agent-browser+Agent) | C+ | 新工具动态和实测，不适合作为系统学习主线。 |

## 建议观看顺序

1. 先看企业落地约束：
   [LangChain 年度报告](https://www.youtube.com/watch?v=KcC1JCiHMk8) -> [从 Claude 小卖部实验破产看 AI 落地真相](https://www.youtube.com/watch?v=vd1XoGasyXw)。

2. 再看知识库与 RAG：
   [RAG 工作机制详解](https://www.youtube.com/watch?v=WWdlme1EAGI) -> [从传统 RAG 到 Agentic RAG](https://www.youtube.com/watch?v=UZs_yOKcw7A) -> [RAGFlow：知识库终极引擎](https://www.youtube.com/watch?v=9x-9-r2ifig) -> [Onyx Agentic RAG](https://www.youtube.com/watch?v=_ndl8_bTF2I)。

3. 然后看可复现应用：
   [Dify 数据查询 Agent](https://www.youtube.com/watch?v=ULK9tlyZPqY) -> [Dify + RAGFlow 混合架构](https://www.youtube.com/watch?v=r3PxNVadt3c) -> [Dify + Tavily DeepResearch Agent](https://www.youtube.com/watch?v=ERR4DaNoaHY) -> [n8n AI 实作](https://www.youtube.com/watch?v=vvqhzbp4J5A)。

4. 最后看开源项目拆解：
   [Agent Browser 源码解析](https://www.youtube.com/watch?v=J2oRlhbQKUk) -> [Chaterm 运维 Agent](https://www.youtube.com/watch?v=pZmMyu4qaHg) -> [Agentic RAG 源码解析](https://www.youtube.com/watch?v=TUP3Qrq0XKk)。

## 降权规则

直接降权：

- “一人公司”“自动赚钱”“70 个 Agent 替代团队”“24 小时无人运营”这类标题。
- 只展示工具结果，不讲输入数据、失败案例、权限边界、人工确认。
- 自动发公众号、自动发小红书、自动外呼、自动改服务器这类高风险动作，但不讲审核和回滚。
- 把多 Agent 当成默认答案，却没有解释单 Agent / workflow 为什么不够。
- 没有源码、没有流程图、没有验证命令、没有业务闭环的“案例视频”。

可以看但要带脑子看：

- Dify / n8n / Coze 这类 no-code 工具教程。它们能快速搭原型，但企业落地还要补权限、日志、评估、部署和数据治理。
- RAGFlow 这类 RAG 引擎教程。它能解决知识库质量问题的一部分，但不能替你解决业务权限、数据治理、检索评估和人工审核。
- 框架横评视频。横评适合建立地图，不适合替你做技术选型。
- 开源项目介绍视频。先看视频判断方向，再回 GitHub 看代码和维护状态。

## 后续可拆的开源方向

这些可以放到 `research/open-source-projects/` 里逐个拆：

- Dify：可视化 LLM 应用与工作流平台。
- n8n：开源工作流自动化平台，适合业务流程编排。
- RAGFlow：开源 RAG 引擎，重点拆文档解析、切分、召回、引用溯源、RAG workflow 和 Dify 集成边界。
- LangGraph / LangChain：状态化 Agent、图编排、工具调用、Deep Agents。
- AutoGen / CrewAI：多 Agent 协作框架，适合做历史路线和对比。
- Onyx：企业搜索 / 知识库 / Agentic RAG 方向。
- Agent Browser：浏览器自动化 Agent，重点看权限和安全模型。
- Chaterm：DevOps / terminal agent，重点看审计、人审和最小权限。

## 官方/项目校准资料

- RAGFlow GitHub：https://github.com/infiniflow/ragflow
- RAGFlow 官方文档：https://ragflow.io/docs/dev/
- RAGFlow 云服务入口：https://cloud.ragflow.io

RAGFlow 官方仓库当前描述显示，它是开源 RAG engine，并且融合 RAG 与 Agent 能力；官方特性强调 deep document understanding、template-based chunking、grounded citations、heterogeneous data sources、automated RAG workflow。后续看中文视频时，所有部署步骤和功能说法都要回到这些官方资料校准。

## 还没验证什么

- 这份清单只是基于 2026-05-08 的 YouTube 检索结果、标题、频道、主题相关性筛选，没有逐条完整观看。
- OpenClaw / Hermes Agent / Agent Browser / Chaterm 等项目需要后续单独核实官方 repo、license、维护状态和安全风险。
- Dify、n8n、RAGFlow、LangGraph、Onyx 等项目需要回到官方文档和 GitHub 校准版本，不要只跟视频操作。
- RAGFlow 相关视频里不少标题强调“命中率最高”“医疗问诊”“企业级”，这些都要后续验证：数据集是什么、评估指标是什么、召回/重排怎么做、引用是否可靠、是否支持权限隔离。
- 后续观看每个视频时，建议补充：业务场景、输入输出、数据来源、是否有源码、能否复现、失败边界、是否需要人审。
