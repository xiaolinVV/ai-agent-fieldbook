# 中文 AI Agent 技术栈 YouTube 学习清单

日期：2026-05-08

## 今天筛了什么

本次筛选目标是找中文 YouTube 上和 OpenAI Agent、Anthropic Agent 技术栈相关的高质量教学视频或高质量博主。

检索关键词：

- `OpenAI Agents SDK 中文 教程`
- `OpenAI Responses API Agents SDK 中文`
- `Claude Code 中文 教程 Agent`
- `MCP Claude Anthropic 中文 教程`
- `Anthropic 官方课程 中文字幕 Claude MCP`
- `OpenAI Agent Builder AgentKit 中文 教程`
- `AI Agent 原理 构建 中文 Claude Code`

核心判断：

- 中文 YouTube 里，Claude Code / MCP / Anthropic 方向的内容质量明显高于 OpenAI Agents SDK 方向。
- OpenAI 方向中文内容偏少，很多是新闻解读或产品演示，必须用官方文档校准。
- 播放量不能直接代表质量。标题里有“吊打”“三分钟颠覆”“一人公司 AI 员工”“70 个 Agent 替代团队”的内容默认降权。

## 第一优先级

已沉淀：

- [Agent 的概念、原理与构建模式：从零打造一个简化版的 Claude Code](Agent%20的概念、原理与构建模式：从零打造一个简化版的%20Claude%20Code.md)
- [实战体验OpenAI全新AI应用开发套件 - Responses API与Agents SDK](实战体验OpenAI全新AI应用开发套件%20-%20Responses%20API与Agents%20SDK.md)

| 顺序 | 视频 | 频道 | 适合学什么 | 判断 |
|---|---|---|---|---|
| 1 | [Agent 的概念、原理与构建模式：从零打造一个简化版的 Claude Code](https://www.youtube.com/watch?v=GE0pFiFJTKo) | 马克的技术工作坊 | Agent 底层原理、Claude Code 类工具怎么运作 | 必看。中文里少见的原理型资源，不只是工具演示。 |
| 2 | [Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 上下文处理 / 权限](https://www.youtube.com/watch?v=AT4b9kLtQCQ) | 马克的技术工作坊 | Anthropic / Claude Code 技术栈全貌 | 必看。覆盖面完整，适合建立 Claude Agent 工程图谱。 |
| 3 | [实战体验 OpenAI 全新 AI 应用开发套件：Responses API 与 Agents SDK](https://www.youtube.com/watch?v=YA2fwTZz0tU) | 01Coder | OpenAI Responses API、Agents SDK 入门实操 | OpenAI 方向优先看这个。 |
| 4 | [从零开始入门 OpenAI 全新 Responses API \| Python](https://www.youtube.com/watch?v=DsOnUiXcQk0) | 技术蛋老师 | OpenAI Responses API 基础 | 先把 API 调用吃透，再谈 Agent。 |
| 5 | [带你免费体验 OpenAI Agents SDK！多代理人工作流超简单上手](https://www.youtube.com/watch?v=xWKzjvhBl3k) | 10 程式中 | OpenAI Agents SDK 快速体验 | 适合看 SDK 怎么跑起来，但别只停在 demo。 |
| 6 | [用 Claude Code 搭建工作流：Sub-agent + Slash Commands](https://www.youtube.com/watch?v=WJ-wRiUQg_0) | huangyihe | Claude Code 工作流、Sub-agent、命令组织 | 短而聚焦，适合进阶补课。 |
| 7 | [这可能是 Claude Code 最重要的功能：Sub-agents](https://www.youtube.com/watch?v=jRfEWoztxxk) | huangyihe | Sub-agent 机制 | 适合专门补 Claude Code 多代理分工。 |
| 8 | [Claude Code: 从零搭建你的 AI 工作团队（Skills + Agents）](https://www.youtube.com/watch?v=Oi8JtWtZHvA) | 回到 Axton | Claude Code Skills、Agents、工作流 | 偏实操，可以作为 Claude Code 进阶教程。 |

## Anthropic / MCP 中文资源

| 视频 | 频道 | 怎么看 |
|---|---|---|
| [【中文字幕】Anthropic 官方课程（一）：Building with Claude API](https://www.youtube.com/watch?v=Ar--e78apzw) | smithjohn 铜匠学 AI 总比种地强 | 低播放量，但价值在官方课程中文字幕。先看这个打 Claude API 基础。 |
| [【中文字幕】Anthropic 官方课程（二）：Introduction to MCP](https://www.youtube.com/watch?v=qLf_MOFPgrk) | smithjohn 铜匠学 AI 总比种地强 | MCP 入门，建议配合 MCP 官方文档看。 |
| [【中文字幕】Anthropic 官方课程（五）：MCP Advanced Topics](https://www.youtube.com/watch?v=tztvWja69kI) | smithjohn 铜匠学 AI 总比种地强 | MCP 进阶，适合已经知道 tools/resources/prompts 是什么之后看。 |
| [【中文字幕】Anthropic 官方课程（十一）：Claude Code in Action](https://www.youtube.com/watch?v=_xKoMaeHW-Y) | smithjohn 铜匠学 AI 总比种地强 | Claude Code 实战官方课的中文入口。 |
| [AI 小白入门：MCP 是什么？怎么用？概念 + 实战讲解](https://www.youtube.com/watch?v=NCtc5lIV7pM) | 木子 AI 研究所 | 入门友好，但技术深度一般。用来建立概念，不要当最终依据。 |
| [如何去编写一个 MCP？Anthropic 官方教程“逐字稿”](https://www.youtube.com/watch?v=vOICqYoCtWo) | AI 产品自由 | 如果要自己写 MCP server，可以看。标题朴素，方向对。 |
| [为什么越来越多的人抛弃 MCP，转向 CLI？](https://www.youtube.com/watch?v=NApOvFHCb8s) | 马克的技术工作坊 | 值得看。不是所有东西都该 MCP 化，能避免过度设计。 |

## OpenAI Agent Builder / AgentKit 方向

这组更偏产品化、低代码和工作流，不是 SDK 工程核心。可以看，但不放在最前面。

| 视频 | 频道 | 判断 |
|---|---|---|
| [45 分钟掌握 OpenAI Agent Builder，建造自己的 AI Agent 团队](https://www.youtube.com/watch?v=cTa_JeoEEdQ) | 汉克蔡 \| Ai 集 | 适合了解 OpenAI Agent Builder 的产品形态。 |
| [认识 AgentKit：替你的网站加上 AI 聊天机器人](https://www.youtube.com/watch?v=g1Rzx9MDr3M) | ChaoCode | 适合前端/网站集成视角。 |
| [40 分钟学会 OpenAI Agent Builder 完整教学](https://www.youtube.com/watch?v=kUZ9-zme5U0) | 李哈利 Harry | 新手友好，偏操作教程。 |
| [对标 n8n？OpenAI 新一代 AI 工作流：Agent Kit 实战教程 + 深度对比 n8n](https://www.youtube.com/watch?v=6dNPMzHNbvM) | 陶渊小明 | 可以看产品比较，但不要把它当底层技术课。 |
| [OpenAI Agent Builder 登场！跟 Dify 比较](https://www.youtube.com/watch?v=FWBnda4_0ts) | 阿石 OMP | 适合了解 Agent Builder 与现有工作流平台差异。 |

## 值得关注的中文频道

| 频道 | 推荐级别 | 原因 |
|---|---:|---|
| [马克的技术工作坊](https://www.youtube.com/results?search_query=%E9%A9%AC%E5%85%8B%E7%9A%84%E6%8A%80%E6%9C%AF%E5%B7%A5%E4%BD%9C%E5%9D%8A+Claude+Code+Agent) | S | 当前中文 YouTube 里讲 Agent 原理、Claude Code、MCP 最值得优先看的频道之一。 |
| [01Coder](https://www.youtube.com/results?search_query=01Coder+OpenAI+Responses+API+Agents+SDK) | A | OpenAI API / Agent 实操比较直接，适合写代码的人。 |
| [huangyihe](https://www.youtube.com/results?search_query=huangyihe+Claude+Code+Sub-agent) | A | Claude Code 工作流、Sub-agent 讲得比较聚焦。 |
| [技术蛋老师](https://www.youtube.com/results?search_query=%E6%8A%80%E6%9C%AF%E8%9B%8B%E8%80%81%E5%B8%88+OpenAI+Responses+API) | B+ | 适合补 OpenAI API / Python 基础。 |
| [回到 Axton](https://www.youtube.com/results?search_query=%E5%9B%9E%E5%88%B0+Axton+Claude+Code+Agents+Skills) | B+ | Claude Code、Skills、Agents 实操可以看。 |
| [smithjohn 铜匠学 AI 总比种地强](https://www.youtube.com/results?search_query=smithjohn+Anthropic+%E5%AE%98%E6%96%B9%E8%AF%BE%E7%A8%8B+%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95) | B+ | 价值在搬运/翻译官方课程，播放量低不是问题。 |
| [唐国梁 Tommy](https://www.youtube.com/results?search_query=%E5%94%90%E5%9B%BD%E6%A2%81+OpenAI+Agents+SDK+Claude+Code) | B | 主题多，部分视频偏硬核，但标题有时过满。挑源码/案例类看。 |
| [汉克蔡 \| Ai 集](https://www.youtube.com/results?search_query=%E6%B1%89%E5%85%8B%E8%94%A1+OpenAI+Agent+Builder) | B | 适合 Agent Builder / 工具型教程，不是底层工程主线。 |
| [阿石 OMP](https://www.youtube.com/results?search_query=%E9%98%BF%E7%9F%B3+AI+Agent+OpenAI+Agent+Builder) | B | 适合初学者理解工具选型，技术深度有限。 |
| [NiceKate AI](https://www.youtube.com/results?search_query=NiceKate+OpenAI+Agent+Claude+Code) | C+ | 适合看动态和新品，不建议作为系统学习主线。 |

## 建议观看顺序

1. 先看 [Agent 的概念、原理与构建模式](https://www.youtube.com/watch?v=GE0pFiFJTKo)。
   先搞懂 Agent 到底是什么，不然看再多工具演示也只是热闹。

2. 再看 OpenAI 方向：
   [01Coder 的 Responses API + Agents SDK](https://www.youtube.com/watch?v=YA2fwTZz0tU) -> [技术蛋老师 Responses API](https://www.youtube.com/watch?v=DsOnUiXcQk0) -> [10 程式中 Agents SDK](https://www.youtube.com/watch?v=xWKzjvhBl3k)。

3. 然后看 Anthropic / Claude Code：
   [Claude Code 从 0 到 1 全攻略](https://www.youtube.com/watch?v=AT4b9kLtQCQ) -> [Sub-agent + Slash Commands](https://www.youtube.com/watch?v=WJ-wRiUQg_0) -> [Skills + Agents](https://www.youtube.com/watch?v=Oi8JtWtZHvA)。

4. 最后补 MCP：
   [Introduction to MCP 中文字幕](https://www.youtube.com/watch?v=qLf_MOFPgrk) -> [MCP Advanced Topics 中文字幕](https://www.youtube.com/watch?v=tztvWja69kI) -> [如何编写一个 MCP](https://www.youtube.com/watch?v=vOICqYoCtWo)。

## 直接降权的内容

- 标题里有“吊打”“三分钟颠覆”“70 个 Agent 替代团队”“一人公司 AI 员工”的，默认降权。
- 只演示 Claude Code / Agent Builder 点点点，不讲权限、上下文、失败处理、工具边界的，最多当工具上手视频。
- 还在主推旧的 OpenAI Assistants API，又不解释 Responses API / Agents SDK / AgentKit 差异的，不当主线学。
- MCP 教程如果只教连数据库、连文件系统、连 GitHub，但不讲权限隔离和人审，不学这种习惯。

## 官方校准资料

中文视频可以帮入门，但最终要用官方资料校准，否则 API 一更新就会被旧教程带偏。

- OpenAI Agents SDK 官方文档：https://developers.openai.com/api/docs/guides/agents
- OpenAI agent 工具发布说明：https://openai.com/index/new-tools-for-building-agents/
- Anthropic Building effective agents：https://www.anthropic.com/engineering/building-effective-agents
- MCP 官方文档：https://modelcontextprotocol.io/docs/getting-started/intro

## 还没验证什么

- 这份清单只是基于 2026-05-08 的 YouTube 检索结果和标题/频道/主题筛选，没有逐条完整观看。
- 后续观看时，需要为每个视频补充：核心观点、是否过时、是否有代码、是否能复现实验、是否符合官方文档。
- OpenAI 方向变化快，观看时必须对照最新官方文档确认 API 名称和 SDK 用法。
