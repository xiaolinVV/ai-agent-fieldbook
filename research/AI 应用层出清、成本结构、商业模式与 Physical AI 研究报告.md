# AI 应用层出清、成本结构、商业模式与 Physical AI 研究报告

## 执行摘要

这份报告的核心判断不是“AI 应用不行了”，而是：**第一轮低壁垒、弱闭环、强补贴、弱付费的 AI 应用正在出清；而入口型、工作流型、开发者型、强约束垂直场景，以及一部分端侧与物理世界 AI，仍在建立长期价值。** 公开材料显示，行业主流公司过去一年更像是在做“产品整合、入口集中、计费重构、从聊天转向执行”，而不是全面撤退。OpenAI 一边下线旧形态插件、强化 ChatGPT 平台化与企业连接能力，一边推出 deep research、Deployment Company；Google 把 Assistant 升级为 Gemini，并把 Gemini 整合进 Workspace 与 Search；Microsoft 把销售、服务、财务 Copilot 并入 Microsoft 365 Copilot；阿里把 Quark 升级为旗舰 AI super assistant；腾讯把 AI 能力加速嵌入微信与元宝；字节则一边整合部分产品线，一边继续扩大模型与应用投入。citeturn27search3turn27search1turn26search1turn23news36turn28search6turn28search10turn29search6turn29news33turn39view0turn39view1

更直白地说，**泡沫破裂的是“AI wrapper 式应用套利”**：没有入口、没有专有数据、没有工作流控制点、没有权限体系、没有评估闭环、还要靠高频免费使用去堆 DAU 的产品，最容易出现“用户越多，亏得越快”。公开计费文档已经说明，今天一个 AI 任务不仅消耗模型 token，还会消耗搜索调用、容器/虚拟机执行、第三方 API、知识库存储与检索等资源；这和传统 SaaS 主要增加数据库、带宽、客服支出而不是“每次核心计算都持续计费”的成本结构不同。citeturn33search0turn32search1turn32search2turn31search7

“传统移动互联网打法”在 AI 上失灵，并不是因为“AI 没需求”，而是因为**获客、留存、成本、验证、付费链路同时变化**。在移动互联网时代，很多产品可以先用极低边际成本换规模，再靠广告、会员、电商、增值服务变现；而在 AI 时代，核心能力本身就持续消耗算力，免费规模经常直接放大亏损。所以真正强势的玩家，要么有入口来摊薄获客成本并提高留存，要么能把 AI 嵌进高价值、高频、可验证、可审计的业务动作里，要么拥有真实世界的数据与执行闭环。Google 的 AI Overviews 已触达 15 亿月用户，OpenAI 在 2025 年 2 月已超过 4 亿周活，Microsoft、Google、Apple 也都把 AI 深度并入原有产品面；这些都说明“入口 + 平台 + 付费通道”比孤立 App 更能承受 AI 的成本结构。citeturn23search0turn23search2turn23search3turn28search6turn38view1

对你新增的两个方向，我的明确判断是：**“垂直工作流控制点”应被单独列为第四方向，而且在很多 ToB 场景里，它比“垂直数据壁垒”更重要；“物理 AI / Physical AI”也应单独列为第五方向，而不是简单并入“硬件 + AI 绑定”。** 原因在于，“硬件 + AI 绑定”只说明 AI 被装进设备、OS、手机、眼镜、PC、车载等硬件体系；但“Physical AI”要求系统能在真实物理世界里完成感知、推理、规划、动作、反馈闭环，并面对安全、延迟、维护、仿真、部署与责任归属问题。NVIDIA 明确把 Physical AI 定义为让机器人、摄像系统、自动驾驶车等自主系统在物理世界中“感知、理解、推理并执行复杂动作”；同时又把它和只在数字环境中运行的 agentic AI 区分开来。citeturn37view2turn37view0

因此，本报告给出的五条长期主线是：**模型 + 入口、垂直数据壁垒、硬件 + AI 绑定、垂直工作流控制点、Physical AI。** 其中第三条与第五条相关，但不等价。AI 手机、AI PC、智能眼镜、车机、空间计算设备可以归入“硬件 + AI 绑定”；而仓储机器人、自动驾驶、工业自动化、无人机巡检、智能安防、自主作业设备等，更适合归入“Physical AI”。前者强调分发与终端承载，后者强调现实世界执行。citeturn38view0turn38view2turn38view4turn37view2turn37view4

下表给出本报告的八条最重要结论：

| 结论 | 明确判断 | 证据锚点 |
|---|---|---|
| AI 应用层是否泡沫破裂 | **部分破裂，不是整体破裂** | citeturn39view1turn27search3turn23news36turn28search6 |
| 破裂的是哪类 | **低壁垒通用 wrapper、无入口 DAU 型、弱付费 C 端、伪标准化 ToB 定制化产品** | citeturn31search7turn33search0turn32search1turn20search7turn21search15 |
| 仍值得长期投入的方向 | **入口型、工作流型、开发者工具、强约束垂直场景、基础设施、部分端侧与 Physical AI** | citeturn23search2turn20search1turn19search13turn21search8turn37view1 |
| 为什么移动互联网打法失灵 | **AI 的核心能力本身持续计费，免费规模会放大亏损** | citeturn33search0turn32search1turn32search2turn31search7 |
| ToB AI 为什么容易项目制 | **权限、流程、合规、例外处理、评估、系统集成差异太大** | citeturn20search6turn21search15turn20search7turn21search8 |
| “垂直数据”与“工作流控制点”谁更重要 | **多数企业场景里，工作流控制点更重要；强数据壁垒往往是工作流运行后的副产物** | citeturn21search9turn21search15turn21search8turn20search2 |
| Physical AI 是什么 | **不是具身智能的简单别名，也不等于所有 AI 硬件，而是“在物理世界可执行”的自主系统范式** | citeturn37view2turn34search6turn37view4 |
| Physical AI 应归入哪里 | **应单列为第五方向；在资本叙事上是“硬件 + AI”的升级版，在研究框架上是独立主线** | citeturn37view0turn37view2turn34search8turn37view4 |

## 事实核验

先说最关键的结论：**“字节砍掉 30% AI 应用项目”目前没有找到可靠的一手公开证据。** 我找到的最接近事实的公开信息，是字节 AI 产品部门 Flow 在 2025 年 4 月出现过产品与组织调整：据 LatePost 报道并被 36 氪转述，猫箱负责人离职，星绘团队计划并入豆包，由豆包方向统一管理；这说明“整合与聚焦”是真实存在的，但不足以推出“砍掉 30% AI 项目”这一带比例、带全局战略含义的结论。与此同时，Reuters 在 2025 年 1 月的报道还提到，字节当时仍拥有 15 个以上 standalone AI 应用，并继续把 AI 视为重点投入方向；字节也对匿名来源的 AI 支出数字公开表示“信息不准确”。因此，这条“30%”更接近**传闻放大版的组织整合叙事**，不是目前可证实的事实。citeturn39view1turn39view0turn39view2

“2025 年 AI 推理成本超过 80 亿，是营收 2.3 倍”这一说法，同样**没有找到可靠公开信源，也无法确认口径**。问题不在于“AI 推理一定不贵”，而在于这个数字缺少最基本的定义：是人民币还是美元、是模型 API 还是自有应用、是增量收入还是 AI 业务总收入、是仅推理还是包含训练与基础设施。更重要的是，ByteDance 是未上市公司，没有公布这种可核对的明细口径；而 Reuters 同期两次报道称，字节分别出现了匿名披露的 AI 基建投入计划，但字节官方都否认这些匿名口径准确。公开可见的反向信号是：公司在 2025 年仍进行超过 3300 亿美元估值的员工回购，2026 年 2 月二级市场股权交易对公司的估值又被推到约 5500 亿美元，这显然不能证明“现金流撑不到 2027”。所以更严谨的结论是：**AI 成本承压是真的，但“80 亿、2.3 倍、现金流见底”这组说法未获公开验证。** citeturn39view2turn39view0turn41search1turn41search0

“原计划新增 3 个千万 DAU 产品全失败”也**没有找到公开证据链**。目前公开可核的反证是：Reuters 在 2026 年 2 月援引 AICPB 数据称，豆包 App 在 2 月 16 日已突破 1 亿 DAU；Reuters 在更早的报道里也点名了字节多个仍在运营的 AI 产品，包括豆包、即梦、星绘、扣子、猫箱等。再结合 36 氪对星绘并入豆包、火山写作并入豆包的梳理，更合理的结论不是“全失败”，而是：**多条产品线中，有的跑出来了，有的被整合了，有的作为能力模块而不是独立 App 存活。** 这与大厂在新赛道常见的“赛马—整合—归核”机制一致。citeturn28search2turn39view0turn39view1turn30search0

如果把视角扩大到整个行业，过去一年公开可证实的主旋律不是“AI 应用全面收缩”，而是**平台化整合与计费重构**。OpenAI 已明确弃用插件生态，转向 GPTs、ChatGPT apps 与企业连接能力，同时把 deep research、运营代理与企业部署组织并到更完整的平台中；Google 把移动端 Assistant 升级为 Gemini，并把 Gemini 纳入 Workspace 和 Search；Microsoft 把 Sales、Service、Finance Copilot 并入 Microsoft 365 Copilot；Baidu 则在竞争压力下把 Ernie Bot 改为免费并继续强调 AI Applications 收入；阿里把 Quark 明确升级为旗舰 AI super assistant；腾讯将 AI 搜索和元宝能力嵌入微信生态。这些动作更像是**收缩重复 SKU、强化入口与控制面**，而不是否定 AI 应用本身。citeturn27search3turn26news14turn28search6turn28search10turn23search3turn29news32turn36search10turn29search6turn29news33

关于孙宇晨与“Physical AI”，我能确认的事实比中文二手稿件要窄一些。可确认的部分是：**孙宇晨的官方 X 账号确实公开使用了“物理 AI / Physical AI”的表达。** 检索到的官方帖子摘要显示，他在中文账号中写过“**四件事拼在一起，就是物理 AI 的全图景**”；在其他公开帖文里，他也把 AI 的未来与支付环境、Agent 服务、链上身份和结算基础设施联系起来。TRON 方面早在 2023 年就宣布过 1 亿美元 AI Development Fund，2026 年又把 AI Fund 扩至 10 亿美元，并把 B.AI 定义为面向 AI agent 的模型访问、支付、结算、身份与协同基础设施。citeturn14search0turn12search2turn13search21turn13search20turn13search1

但需要非常明确地说：**我们没有在可访问公开材料中找到一份足够完整的一手视频全文，能够逐字还原“Physical AI”那段观点的全部上下文。** 目前流行的“具身智能、无人机、空间计算、太空探索”等拆解，主要出自 HTX、MarsBit、Odaily、Panews 等二次整理文章，而不是一个公开可直接校验的完整原始口述文本。这意味着：可以确认孙宇晨公开采用了“Physical AI”这一叙事框架；但“他究竟把它严格定义为哪些方向”，目前更多还是**部分一手 + 大量二手加工**。citeturn14search0turn11search2turn9view1turn11search14turn11search18

综合信源分级如下：

| 命题 | 当前结论 | 信源等级 | 备注 |
|---|---|---|---|
| 字节砍掉 30% AI 应用项目 | **未证实** | 中低 | 有产品整合公开线索，但无“30%”一手证据 citeturn39view1turn39view0 |
| 字节 2025 AI 推理成本超 80 亿、为营收 2.3 倍 | **未证实** | 低 | 无可靠口径，且与公开财务/估值信号不吻合 citeturn39view2turn41search1turn41search0 |
| 原计划 3 个千万 DAU 产品全部失败 | **未证实** | 低 | 未找到产品清单与公开达标/失标证据 citeturn28search2turn39view0 |
| 字节存在 AI 产品整合与聚焦 | **已证实** | 中高 | 星绘并入豆包、火山写作并入豆包等线索清晰 citeturn39view1turn30search0 |
| 孙宇晨公开使用 “Physical AI” 表述 | **基本证实** | 中 | 有官方 X 帖文摘要，但上下文不完整 citeturn14search0turn11search2 |
| 孙宇晨把 Physical AI 明确拆成若干子方向 | **部分证实** | 中低 | 细分拆解主要来自二手整理稿 citeturn9view1turn11search14turn11search18 |
| 孙宇晨把 AI 与支付 / Agent 经济相连 | **已证实** | 中高 | 官方 X 与 TRON/B.AI 资料可验证 citeturn12search2turn13search20turn13search21 |

## 成本结构与单位经济

AI 应用和传统 SaaS 最大的差别，不在“是不是软件”，而在**核心价值交付的每一次执行都在持续消耗昂贵计算资源**。OpenAI 的官方 API 定价把输入 token、缓存输入、输出 token、web search 调用、容器执行都单独计费；Anthropic 也把输入、输出、prompt caching、batch processing 单独列价；Google Gemini 则把 grounded search 明确定义为额外收费项；字节扣子文档甚至直接把“大语言模型、虚拟机、第三方 API、知识库空间”等全部列为 AI 任务成本来源。也就是说，AI 应用不是简单地“多一点服务器费”，而是每一个任务都在触发一串实时成本事件。citeturn33search0turn32search1turn32search2turn31search7

一个简化但足够实用的软件 AI 单位经济模型，可以写成：

**单次任务毛利 = 用户愿意支付的任务价值 − 模型推理成本 − 检索/存储成本 − 工具调用/API 成本 − 人工复核成本 − 客服与交付成本 − 获客成本摊销。**

如果用当前公开价格做示意：以 OpenAI GPT-5.4 为例，输入价格约为每百万 token 2.5 美元、输出为 15 美元；Anthropic Claude Sonnet 4.6 为输入 3 美元、输出 15 美元；Google 则会对 grounding search 单独收费。一个看似很小的“8k 输入 + 2k 输出 + 1 次搜索”的任务，在高质量模型上就已经出现可感知的边际成本；如果再叠加长上下文、多轮 agent 调用、容器执行和第三方服务，单次任务成本会迅速上升。于是，“免费获客、鼓励高频使用、先堆 DAU 再说”的玩法，很容易变成**增长越成功、亏损越确定**。citeturn33search0turn32search1turn32search2

这就是为什么“DAU 陷阱”在 AI 时代比移动互联网时代更危险。OpenAI 要把 deep research 拆成标准版与 lightweight 版，本质就是在降低高复杂任务的推理成本；GitHub 从 2026 年开始把 Copilot 转向 usage-based billing，本质也是把 AI 资源消耗和供给约束更清晰地映射到价格上；Microsoft、Google 则更偏向把 AI 作为已有入口与订阅体系的增值层来卖，而不是让独立新 App 长期免费烧钱。大厂能承受这种结构，是因为它们有搜索、办公、OS、浏览器、代码平台、手机等“前置入口”来降低获客和提高留存；创业公司则很难同时承担高获客成本和高推理成本。citeturn32news31turn20search12turn23search3turn28search10turn23search2

与之相对，传统软件的边际成本更低，因为新增一个用户，很多时候增加的是数据库存储、消息队列、API 带宽和客服支出，而不是持续执行一段高代价“推理”。这并不意味着传统软件没有成本，而是说它更接近“固定成本 + 弱变量成本”的结构。AI 应用则更像“固定成本 + 强变量成本”。所以，真正重要的不是“模型会不会继续降价”，而是**你的产品能否把昂贵推理集中到高价值任务、可验证动作和可付费环节上**。模型降价会改善单位经济，但不能自动修复低价值任务、低转化率和高人工干预的问题。citeturn33search0turn32search1turn20search7turn21search8

AI 应用的成本控制手段，今天已经相当明确：第一，用更小、更便宜、更快的模型处理大多数请求，只把少数高风险任务升级到强模型；第二，用 prompt caching、上下文压缩、检索前置过滤来减少重复 token；第三，用 batch、异步和后台处理降低实时成本；第四，把动作执行和知识检索标准化，减少 agent 在低价值路径上的无效探索；第五，在合适场景把推理下沉到端侧，以降低时延和云成本、提升隐私与可用性。OpenAI 官方写明 Batch API 可节省 50%，Anthropic 官方写明 prompt caching 最多可节省 90%，Google DeepMind 直接把 on-device robotics 的价值归为低时延、低依赖网络、适合安全与连接受限场景。citeturn33search0turn32search7turn37view5

物理 AI 的单位经济模型则不同。它可以写成：

**单次物理任务毛利 = 用户愿意支付的任务价值 − 硬件折旧 − 端侧/云侧推理成本 − 传感器与边缘计算成本 − 数据采集与标注摊销 − 设备维护成本 − 现场交付与售后成本 − 安全验证与合规成本 − 获客成本摊销。**

注意它**并没有“摆脱成本问题”**，只是把主要矛盾从纯 token 成本，转移到“硬件 + 安全 + 维护 + 部署 + 仿真 + 供应链”上。NVIDIA 明确指出，Physical AI 需要高保真 physics-based simulation、digital twin、synthetic data、world foundation models 和训练—仿真—端侧推理三台“计算机”；Google DeepMind 则强调 VLA/ER/on-device 组合、低时延与本地运行；Apple 在 Apple Intelligence 上也把“先端侧、复杂任务再上私有云”作为基本架构。换句话说，Physical AI 避开的不是成本，而是**“云端 token 直接随免费 DAU 爆炸”**这一单一矛盾。citeturn37view2turn37view0turn34search8turn37view5turn38view1

把不同形态的风险放在一起比较，会更清楚：

| 类型 | 变量成本强度 | 交付复杂度 | 规模化难点 | 最常见失败方式 |
|---|---:|---:|---:|---|
| 通用聊天 App | 高 | 低 | 获客与付费 | DAU 高、付费低、成本失控 |
| 内容生成工具 | 很高 | 低 | 版权/质量/转化 | 使用高峰时毛利塌陷 |
| 企业知识库 / RAG | 中 | 中 | 权限与评估 | 回答看似可用，实际不可审计 |
| 工作流 Agent | 中高 | 高 | 集成、状态、异常处理 | 从产品退化成定制项目 |
| 代码 Agent | 中高 | 中 | 仓库上下文、安全治理 | 演示惊艳，复杂仓库落地差 |
| AI 硬件 | 中 | 高 | 渠道、OS、供应链 | 只做卖点，不形成留存 |
| Physical AI | 中 | 很高 | 可靠性、维护、安全、ROI | Demo 酷、部署慢、售后重 |

这张表是对公开产品定价、企业平台能力与机器人/自动驾驶部署案例的归纳：软件 AI 主要死于“边际成本高 + 缺入口 + 弱付费”；Physical AI 主要死于“产品太重 + 交付太慢 + 安全责任太高”。前者是算力毛利问题，后者是系统工程与产业化问题。citeturn33search0turn32search1turn31search7turn20search6turn21search15turn17search6turn18search0turn35news34

## 应用分层与五条主线

如果把现阶段 AI 产业按“谁付费、是否有入口、是否有动作闭环、是否依赖真实世界反馈”来拆，而不是按“是否用了大模型”来拆，应用地图会更清楚。下表综合了公开产品路线、定价文档、企业功能披露与机器人/自动驾驶部署进展，对你要求的 11 类对象做了一个适合长期跟踪的归纳。citeturn23search2turn23search3turn20search1turn19search13turn21search8turn21search15turn29search6turn36search10turn37view2turn37view4

| 类别 | 主要用户 | 主要任务 | 主要壁垒 | 最大风险 | 未来三年判断 |
|---|---|---|---|---|---|
| C 端通用聊天助手 | 大众用户 | 问答、检索、陪伴、轻办公 | 入口、品牌、分发、模型质量 | 同质化、免费化、成本失控 | **头部集中** |
| C 端内容生成工具 | 创作者/营销/自媒体 | 文案、图像、视频、PPT | 模型效果、场景模板、社区 | 高算力成本、版权与审美趋同 | **会分化，少数活成平台能力** |
| 搜索/浏览器/办公/OS 入口型 AI | 大厂生态用户 | 搜索、总结、写作、协作 | 默认入口、账号体系、分发、订阅 | 创新被平台内耗吞掉 | **最稳健** |
| ToB 企业知识库 / RAG | 企业员工 | 企业搜索、资料问答 | 权限、连接器、可引用性 | “看起来会答，其实不可用” | **会被纳入更大工作台** |
| 垂直工作流 AI | 客服/法务/销售/财务/HR | 审核、执行、编排、记录 | 工作流控制点、审计、状态管理 | 项目制、例外太多 | **长期价值最高之一** |
| 代码生成 / 代码 Agent | 开发者 | 补全、重构、调试、审查 | 仓库上下文、IDE 入口、治理 | 复杂系统失真、权限安全 | **高景气，但平台化加剧** |
| Agent 平台与基础设施 | 开发团队/企业 | 编排、工具调用、评估、观测 | 开发者生态、治理、标准 | 被模型厂商内建替代 | **中长期存在，但会浓缩** |
| 行业级 AI 应用 | 医疗/金融/法律/制造等 | 高价值专业任务 | 合规、标签数据、领域工作流 | 商业周期长、人工必需 | **强者恒强** |
| AI 硬件 / 端侧 AI | 手机、PC、眼镜、车载 | 本地助理、感知、交互 | 终端装机量、芯片、OS、渠道 | 沦为功能卖点 | **会普及，但护城河不一** |
| Physical AI | 机器人、无人机、车、智能设施 | 感知—规划—执行 | 真实世界反馈、控制、安全、维护 | Demo 泡沫、交付重 | **独立主线，但成熟度分化极大** |
| 模型 API / 云 / 推理基础设施 | 开发者、企业、平台 | 模型调用、训练、推理、管理 | 算力、工程优化、生态与价格 | 价格战与资本开支压力 | **仍是基础层高战场** |

在这张地图上，第一条主线“**模型 + 流量入口**”成立，而且更适合大厂。原因很简单：入口能降低获客成本，提高留存，并把 AI 消耗打包进更大的订阅或广告体系。Google 的 AI Overviews 直接建在 Search 上；Google Assistant 正升级为 Gemini；Microsoft 把 Copilot 塞进 Office、Teams、GitHub 和 Azure；Apple 把 Apple Intelligence 建在系统层，把复杂请求经 Private Cloud Compute 处理；阿里的 Quark 也是“搜索/浏览/学习/文档/云盘”一体化入口，而不是一个孤立聊天框。对于绝大多数创业公司来说，**没有入口时，最难的不是做出 AI，而是付得起获客。** citeturn23search2turn28search6turn23search3turn38view1turn29search6

第二条主线“**垂直数据壁垒**”只在特定条件下成立。公开网页、行业 PDF、普通知识库，随着模型能力提升会越来越像公共原料；而真正强的数据壁垒，必须是独占、持续更新、和业务标签绑定、受权限与合规保护、能跟动作结果形成反馈闭环的数据。Glean 强调的是 enterprise permissions、connectors 与 actions，而不是“把文档全喂进去”；Zendesk 强调的是 Resolution Learning Loop，用服务结果持续改进自动化；Harvey 强调的是 firm templates、matter context 与 workflow agents；Hebbia 强调的是可回溯引用、复杂私有数据和高风险决策场景。也就是说，**数据壁垒不是“有一堆文件”，而是“能在正确权限和正确动作里反复利用的数据系统”。** citeturn21search9turn21search12turn21search15turn20search7turn21search8turn21search10

第三条主线“**硬件 + AI 绑定**”依然成立，但它太宽了。AI 手机、AI PC、智能眼镜、AR/VR、车机、智能摄像头都在这里；它们提供分发、端侧算力、上下文感知和设备入口，但并不一定形成现实世界动作闭环。Apple Intelligence、Vision Pro、Meta Ray-Ban / Orion、Google Home/Gemini、AI PC 和 AI 手机，本质上都在证明：端侧并不是“不要云”，而是“把时延、隐私、稳定性和上下文拿回来”。这条主线是 AI 普及的重要载体，但只有当设备成为**持续交互入口或传感器网络的一部分**时，才会显著提升护城河。citeturn38view1turn38view0turn38view2turn38view4turn28search3

第四条主线“**垂直工作流控制点**”是这份报告里最值得单独强调的部分。因为大多数企业并不是缺一个“会回答问题的模型”，而是缺一个**能在权限内完成业务动作、对结果负责、可审计、可回滚、可人工接管**的系统。Glean 的 Actions 文档把这个问题说得很清楚：行动层让 assistant 和 agent 不只是生成文本，而是执行标准化操作；Harvey 的 Workflow Agents 让法律团队把模板、逻辑和输出变成可复用流程；ServiceNow 的 Now Assist Analytics 把 adoption、skill performance、ROI 监控做成产品；Zendesk 则把 AI、知识库与人工坐席放进同一个 resolution loop 里。这些都说明，**比“回答对”更重要的是“能把事情做完”。** citeturn21search15turn21search8turn20search2turn20search6turn20search7

第五条主线“**Physical AI**”则应该独立成章。它和第三条联系紧密，但不能混写。因为“硬件 + AI”强调的是承载关系，而“Physical AI”强调的是执行关系：能否在真实环境中感知、推理、规划、执行、纠错并持续学习。**所以在你的长期研究手册中，我建议把“Physical AI”作为第五条主线独立维护。** 第三条保留做“AI 设备与终端入口”研究，第五条做“物理世界执行系统”研究。citeturn37view2turn37view0turn37view4

## 物理 AI专题

在官方资料里，NVIDIA 对 Physical AI 的定义已经足够清楚：它让机器人、摄像系统、自驾驶汽车等自主系统在物理世界中**感知、理解、推理并执行复杂动作**；NVIDIA 还明确将其与只在数字环境中运行的 agentic AI 区分开来。Google DeepMind 的表达略有不同，但方向一致：Gemini Robotics 以 VLA 模型把视觉信息与语言指令转换为 motor commands，Gemini Robotics-ER 负责 embodied reasoning，on-device 版本负责低时延、本地运行与连接受限场景。换句话说，**Physical AI 不是“更硬一点的 AI”，而是“以真实世界动作闭环为目标的 AI”。** citeturn37view2turn37view0turn37view4turn37view5

为了避免概念混淆，可以把几个术语分开看：

| 概念 | 更准确的含义 | 是否必须有硬件 | 解决的核心问题 |
|---|---|---|---|
| AI Hardware | 带 AI 计算/交互能力的硬件产品 | 是 | 分发、终端承载、算力入口 |
| Edge AI | 模型在设备端或边缘节点推理 | 通常是 | 低时延、隐私、离线可用 |
| Spatial AI | 对 3D 空间、位置、关系的理解 | 不一定 | 让系统理解“空间” |
| World Models | 对物理世界动态规律的建模与仿真 | 不一定 | 训练与预测真实世界演化 |
| Embodied AI | AI 与感知/行动能力结合的物理系统 | 是 | 让系统能“身在世界中”学习与行动 |
| Robotics | 机器人这一具体产品/产业 | 是 | 操作、移动、服务、制造 |
| Autonomous Systems | 各类可自主运行系统的总称 | 通常是 | 在限定/开放环境中自主决策 |
| Physical AI | 在物理世界可持续感知—推理—执行的 AI 范式 | 是 | 现实世界动作闭环 |

这个划分的关键在于：**Physical AI 不是“具身智能”的简单包装，但具身智能可以看成其中最醒目的一个子集。** NVIDIA 的官方例子就不仅包括 humanoid robots，还包括 cameras、AVs、smart spaces；也就是说，Physical AI 可以发生在机器人、无人车、固定摄像系统、仓储设施、工厂、基础设施中，并不要求一定是人形机器人。人形机器人是最吸睛的形态，却不是唯一的落地形态。citeturn37view2turn34search6

这也是我对孙宇晨叙事的评价。**有产业逻辑的部分**在于：他捕捉到了 AI 从纯数字交互向真实世界执行扩展的大趋势，这和 NVIDIA、Google DeepMind、自动驾驶、机器人平台的发展方向是一致的；**有叙事包装色彩的部分**在于：把“具身智能、无人机、空间计算、太空探索”等全部打包成一个投资口号后，很容易忽略不同赛道的商业成熟度和工程难度完全不同。尤其是把区块链支付、Agent 经济、Physical AI 混成一条故事线时，逻辑上并非完全不成立，但它更像一种**资本市场叙事桥接**，而不是当前 Physical AI 落地的主因。今天真正推动 Physical AI 的核心力量，仍然是传感器、仿真、控制、边缘推理、数据闭环、安全验证和场景 ROI。citeturn14search0turn12search2turn13search20turn37view1turn37view5

从公司路线看，NVIDIA 是当前最完整的“Physical AI 平台公司”。它押注的不是某一款机器人，而是 DGX 训练、Omniverse/Cosmos 仿真、Jetson 端侧推理、Isaac/GR00T 机器人基础模型、数字孪生和世界模型的全栈。Google DeepMind 则代表了“模型脑”的前沿：VLA、embodied reasoning、on-device robotics SDK，都在试图把通用多模态模型投射到真实动作控制上。Apple 与 Meta 更像是在做 **Physical AI 的前置接口层**：Vision Pro、Ray-Ban Meta、Orion 提供的是空间计算、可穿戴传感与终端交互能力，自身不一定负责工业级动作执行，但会塑造下一代人机交互入口。citeturn37view1turn37view0turn34search8turn37view4turn37view5turn38view0turn38view2turn38view4

如果看真正的商业化强度，**Physical AI 里最成熟的并不是人形机器人，而是约束更强、任务更窄、ROI 更好算的自主系统。** 例如，DJI Enterprise 和 DJI Dock 已经在测绘、巡检、公共安全、能源、施工等行业形成稳定产品形态；Boston Dynamics 的 Stretch 已在 DHL 实现商业部署，双方 2025 年签署了全球部署 1000 台以上的协议；Agility 的 Digit 在 GXO 场景中已完成超过 10 万个 tote 搬运；Waymo 在 2025 年 5 月就已达到每周 25 万付费行程，并在 2025 全年完成 1400 万次行程；Baidu Apollo Go 在 2025 年第四季度完成 340 万次 fully driverless rides，累计公开乘车在 2026 年 2 月超过 2000 万次。相比之下，人形机器人虽然融资热、演示强，但商业证明大多仍处于“有限场景试点 + 规模部署前夜”。citeturn17search2turn17search8turn17search6turn17search3turn18search0turn18search5turn35search15turn35search0turn36search1turn36search2

Tesla 是一个很好的反例与样本。它的价值不在于“讲了 Physical AI 故事”，而在于把自动驾驶、Robotaxi、Optimus 放进了同一个技术与资本叙事中；但从公开运营结果看，**Robotaxi 的商业成熟度还远没有达到叙事高度**。Reuters 在 2026 年 5 月的实测显示，Tesla 在德州多个城市的 Robotaxi 服务仍有长等待、范围受限、路线异常等问题；这说明自动驾驶属于 Physical AI 中商业空间极大、但安全验证与规模化最难的赛道之一。它不是没机会，而是不能因为资本关注度高，就把“已形成成熟闭环”误判成事实。citeturn35news34turn35search13

Figure、Unitree、智元机器人、银河通用等，则代表了 Physical AI 中不同成熟度层次。Figure 与 BMW 的合作已经进入真实工厂测试甚至阶段性产线贡献；Unitree 走的是“硬件低价化 + 快速出货 + 教育/消费/工业兼顾”的路线，产品可得性强，但严格可验证的企业级 ROI 公开数据仍有限；智元与银河通用都释放出了量产、订单或多城部署的积极信号，但公开信息里第三方审计口径仍不多，因此更适合作为**高潜力、需要继续追踪**而不是“已充分验证”的案例。citeturn17search10turn17search0turn17search1turn17search4turn18search1turn18search3turn18search2turn18search9

你要求的“Physical AI 场景判断表”，我建议如下使用：

| 场景 | 是否属于 Physical AI | 是否必须绑定硬件 | 是否需要端侧推理 | 是否有强商业闭环 | 当前成熟度 | 最大风险 |
|---|---|---|---|---|---|---|
| 工业制造 | 是 | 是 | 常常需要 | 强 | 中高 | 安全、集成、停机损失 |
| 仓储物流 | 是 | 是 | 常常需要 | 强 | 高 | 例外处理、维护密度 |
| 无人机与低空巡检 | 是 | 是 | 高 | 强 | 高 | 监管、事故责任 |
| 自动驾驶 / Robotaxi | 是 | 是 | 极高 | 中高 | 中 | 安全与监管 |
| 农业自动化 | 是 | 是 | 高 | 中高 | 中 | 环境非标、季节性 |
| 医疗设备 / 手术机器人 | 是 | 是 | 高 | 中高 | 中 | 合规与责任极重 |
| 家庭服务机器人 | 是 | 是 | 高 | 弱到中 | 低 | 场景过多、ROI 难算 |
| 商业服务机器人 | 是 | 是 | 中高 | 中 | 中 | 需求伪高频 |
| 智能安防 / 摄像头 | 通常是 | 是 | 常常需要 | 强 | 高 | 误报、隐私合规 |
| 智能眼镜 / 空间计算 | 边缘场景算，核心上更像硬件 + AI | 是 | 中 | 中 | 中 | 需求与内容生态 |
| AI PC / 手机 / 可穿戴 | 通常不算核心 Physical AI | 是 | 中 | 中 | 高 | 变成功能卖点 |
| 太空探索 / 卫星 / 空间机器人 | 是 | 是 | 高 | 低到中 | 低 | 周期长、资本密集 |
| 能源 / 电网 / 港口 / 矿山 | 是 | 是 | 高 | 强 | 中高 | 安全与系统复杂度 |

这张表的含义很重要：**并不是所有带硬件的 AI 都该被归入 Physical AI。** AI PC、手机和很多眼镜产品，更准确地说仍然是“硬件 + AI 绑定”；它们可能为 Physical AI 提供传感、空间理解或终端分发，但并不在多数情况下直接承担物理世界任务闭环。相反，工业、物流、无人机、自动驾驶、智能基础设施已经非常接近 Physical AI 的本义。citeturn37view2turn38view0turn38view2turn17search2turn17search8turn17search6turn18search0turn36search1

所以最后给出一句最明确的结论：**Physical AI 会成为 AI 应用层出清之后的重要资金流向之一，但它不是“逃离软件泡沫的免费午餐”。** 它会把“烧 token”的痛点，改写成“烧硬件、烧交付、烧维护、烧安全验证”。不过，它也更有机会形成更深的护城河，因为一旦一个团队同时拿下了硬件供应链、真实世界数据回流、场景交付和维护网络，后来者复制难度通常比复制一个聊天 App 高得多。对产业研究来说，这正是它值得独立跟踪的原因。citeturn37view1turn17search3turn18search0turn35news34

## ToB 产品化困境

“ToB 企业级 AI 正在慢慢变成人力投入的定制项目，标准化产品收益越来越低”——这个判断**在相当多场景里成立，但不是必然宿命**。之所以容易成立，是因为企业里的“同一个问题”表面上相似，底层却牵涉不同权限、多系统接口、审批规则、异常路径、责任边界和评估标准。一个看似一样的“合同审查”，在不同行业、不同法域、不同模板库、不同审批链上，实际都是不同产品；一个看似一样的“客服自动化”，在不同知识库、工单系统、退款规则、SLA 和合规要求下，也会迅速分裂。Harvey、Glean、ServiceNow、Zendesk 这些成熟玩家都没有把自己包装成“万能聊天框”，而是在不断增强 connectors、actions、workflow builder、analytics、governance 与 permission-aware retrieval，这本身就是对“项目制压力”最直接的回应。citeturn21search8turn21search15turn20search2turn20search6turn20search7

真正容易项目制的，往往是三类 ToB AI 场景。第一类是“知识很复杂、动作很敏感、流程很长”的专业工作流，比如法务、金融、医疗、政府；第二类是“系统存量极重”的中后台场景，比如客服、财务、HR、ERP 周边；第三类是“客户自己也说不清需求”的所谓“企业智能体项目”，最后只能靠乙方不断堆规则与人工陪跑。OpenAI 2026 年专门成立 Deployment Company，并收购/并入交付能力，本身就说明哪怕是最强模型平台之一，也承认企业落地需要大量“deployment engineering”；Salesforce 之所以强调 Agentforce 的 work units、deal 数和 ARR，也是在把“AI 是咨询服务还是产品”这个问题尽量往产品化指标上拉。citeturn23news36turn19search13

要避免退化成软件外包，一个更现实的产品架构是：**产品内核 + 配置层 + 定制层**。产品内核包括权限模型、评估框架、观测系统、动作执行总线、模板与策略引擎；配置层包括场景规则、字段映射、审批链、模型路由、知识连接器；定制层则只解决少数高价值差异。Harvey 的 workflow builder、Glean 的 actions、ServiceNow 的 analytics 与 agentic workflows，本质都在积累“可复用内核”，而不是每来一个客户重写一遍系统。citeturn21search11turn21search8turn21search15turn20search6

长期跟踪时，我建议你把“ToB AI 是否正在产品化”量化成几个指标，而不是只看签单数。最关键的指标包括：**部署复用率**（新客户拿到的能力有多少来自既有模块而非新增开发）、**服务收入占比**、**上线周期**、**自动化渗透率**、**人工接管率**、**异常任务回退率**、**评估通过率**、**单位客户毛利**、**权限/审计事件数**。如果一个客户项目签得越多，研发分支代码越多、交付团队越大、支持债务越高，那它增加的不是产品资产，而是维护负债。citeturn20search2turn20search6turn21search15turn21search8

Physical AI 在这件事上通常更“重”。因为它除了软件定制，还会叠加现场部署、地图/工位/设备适配、安全测试、维护与替换件管理。DHL 与 Boston Dynamics 的长期合作、Agility 在 GXO 的持续运营、Waymo 的车辆制造和车队扩张，都说明真正的规模化不是“卖一台机器”就完成，而是“形成标准场景 + 维保体系 + 数据回流 + 可复制部署包”。所以，**Physical AI 通常比 ToB 软件 AI 更项目制，但一旦标准化成功，壁垒也更高。** citeturn17search3turn17search6turn18search0turn35search15

## 职业与组织能力迁移

第一条网友评论有相当高的命中率：如果一个人对 AI 应用开发的理解仅仅停留在“调 API、写 Prompt、套 LangChain”，那么这部分能力**非常容易被压价、被替代、被内建进平台**。OpenAI、Anthropic、GitHub、Cursor、Glean、Harvey 的产品演化都在说明：真正值钱的不是某个 prompt 小技巧，而是上下文工程、权限治理、动作执行、审计日志、成本控制、评估闭环、模型路由和异常恢复。GitHub Copilot 明确提供 enterprise controls 与 audit logs；Cursor 企业版强调 usage control、admin controls 与 privacy mode；Glean 把 actions 做成标准化执行层；Harvey 把 workflow agents 和 firm knowledge 绑定起来；这说明市场需要的是**“把 AI 放进真实系统的人”**，不是“会把 AI 接出来的人”。citeturn20search1turn20search5turn19search3turn21search15turn21search8

因此，真正会贬值的能力，通常是这几种组合：只会调模型 API、只会拼 prompt、不懂业务数据模型、不懂权限与审计、不懂故障恢复、不懂成本核算、不懂评估与安全边界。相反，更值钱的能力会围绕以下能力簇展开：**业务数据建模、系统架构、高可用与高并发、状态机/工作流设计、权限与审计、模型路由、RAG 与可引用性、在线评估/离线评估、成本观测、HITL 接管、以及与现有系统的深度集成。** 今天企业真正购买的不是“一个会说话的模型”，而是“一个可运行、可管理、可追责的系统”。citeturn20search6turn20search2turn21search15turn21search9turn21search10

对传统后端工程师来说，升级路线不应是“把所有 AI 名词都学一遍”，而应是**把已有系统能力迁移到 AI 执行系统**。第一阶段必须补的是：token/cost 概念、上下文窗口与缓存、检索与权限、模型路由、评估方法、对话/任务状态机、异步执行、审计日志、人工接管设计、失败重试与幂等。第二阶段补的是：agent tool use、MCP/connector 思维、知识库治理、离线回放、线上观测、内容安全与输出约束。第三阶段才是更偏前沿的：多模态、端侧推理、低时延架构、仿真、传感器数据处理、世界模型、机器人软件栈。也就是说，**后端不是被淘汰，而是要从“CRUD + 分布式系统”升级为“AI 执行系统工程”。** citeturn26search3turn33search0turn32search1turn31search7turn37view5

如果一个软件工程师想切入 Physical AI，最实用的起点不是先追人形机器人热搜，而是从四个工程接口进入。第一，**仿真与数字孪生**：NVIDIA Omniverse / Isaac、MuJoCo 这一类环境是最接近“软件工程师能直接贡献”的入口；第二，**边缘推理与系统工程**：低时延、本地运行、断网容错、设备 OTA、日志回传；第三，**感知—规划—执行的数据链路**：视觉、传感器、动作日志、回放与评估；第四，**安全与可靠性**：把“模型会不会答错”升级成“设备会不会做错”。Google DeepMind 的 robotics SDK、NVIDIA 的三台计算机架构、Apple 的端侧 + 私有云原则，其实都在提示同一件事：Physical AI 不是“换个更酷的前端”，而是更重的系统工程。citeturn37view5turn37view0turn37view2turn38view1

给传统后端工程师一个更简洁的 1 年 / 3 年路线图：

| 时段 | 该补什么 | 不必追什么 | 最好产出什么 |
|---|---|---|---|
| 未来 1 年 | RAG、评估、权限、工作流、模型路由、成本观测 | 花哨 agent 名词、孤立 prompt 技巧 | 一个可审计的企业 AI workflow demo |
| 未来 3 年 | 多模态、端侧推理、低时延架构、仿真、传感器/边缘系统 | 只做聊天壳子 | 一个“数字世界 workflow”或“物理世界 simulation + control”项目 |

这个路线背后的逻辑是：**你的护城河仍然来自系统能力，只是系统边界从数据库和消息队列，扩展到了模型、上下文、工具、边缘设备与真实世界反馈。** citeturn20search5turn21search15turn37view5turn37view0

## 案例库、未来三年与研究清单

先给出一个可直接沉淀为研究手册的案例矩阵。下表选择了 20 个案例，覆盖通用入口、开发者工具、ToB 工作流、端侧/硬件与 Physical AI。案例判断分为“核心壁垒”“商业闭环清晰度”“当前判断”和“证据强弱”。citeturn23search0turn23search2turn20search1turn21search8turn37view1turn17search6turn18search0

| 案例 | 所属层级 | 核心壁垒 | 商业闭环清晰度 | 当前判断 | 证据强弱 |
|---|---|---|---|---|---|
| ChatGPT / Deep Research | 通用入口 / 研究代理 | 品牌、用户规模、平台化、企业连接 | 中高 | 平台化最强样本之一，但成本管理持续关键 citeturn23search0turn26search1turn26search3turn26news26 | 高 |
| OpenAI apps / GPT Store | 平台生态 | 分发、开发者生态 | 中 | 说明 OpenAI 在从单工具走向平台 citeturn27search1turn27news33 | 高 |
| Microsoft 365 Copilot | 入口型 AI | Office/Teams 入口、企业账号、订阅 | 高 | 最典型“AI 嵌入存量入口”路线 citeturn23search3turn20news36 | 高 |
| Google Gemini + AI Overviews + Workspace | 入口型 AI | Search、Workspace、Android | 高 | Search/Workspace/Assistant 三位一体，入口价值极强 citeturn23search2turn28search6turn28search10 | 高 |
| Apple Intelligence + PCC | 系统级 AI | OS、端侧硬件、隐私架构 | 中高 | 更像“系统能力层”而非独立 App 生意 citeturn38view1turn16search8 | 高 |
| Claude / Claude Code | 通用模型 + 开发者 | 模型能力、代码场景、企业信任 | 中高 | 在 coding 与企业专业场景里强势上升 citeturn25news21turn25search7turn19search2 | 高 |
| GitHub Copilot | 开发者工具 | GitHub 仓库入口、治理、企业控制 | 高 | 代码 AI 的“平台母体”之一 citeturn20search0turn20search1turn20search8turn20search12 | 高 |
| Cursor | AI-native IDE | IDE 体验、速度、团队规则、usage 控制 | 中高 | 高增长但面临平台内化压力 citeturn19search0turn19search3turn19search6 | 中高 |
| 豆包 / 扣子 / 字节 AI 矩阵 | 通用入口 + 平台 | 内容生态、国内分发、多产品线 | 中高 | 有整合但非撤退；关键在成本与平台化 citeturn39view0turn39view1turn31search7turn28search2 | 中高 |
| Quark | 入口型 AI | 搜索/文档/学习/云盘一体化 | 中高 | 阿里最值得跟踪的 C 端入口之一 citeturn29search6turn29search14 | 高 |
| 元宝 + 微信 AI | 生态嵌入型 AI | 超级 App 入口、社交分发 | 中高 | 单 App 不一定胜，生态内嵌很重要 citeturn29news33turn29search3 | 中高 |
| 百度文心 / 文库 / Apollo Go | 搜索 + 行业应用 + 自动驾驶 | 搜索入口、订阅、Robotaxi 数据闭环 | 中高 | 一家同时覆盖软件 AI 与 Physical AI 的样本 citeturn29news32turn36search10turn36search1turn36search2 | 中高 |
| Salesforce Agentforce | ToB 工作流 | CRM 控制点、企业数据、销售/服务流程 | 高 | 工作流控制点路线的代表例子 citeturn19search13 | 高 |
| ServiceNow Now Assist | ToB 工作流 | ITSM/ESM 控制点、流程、审计 | 高 | “制度化 AI”代表，比聊天更接近执行系统 citeturn20search6turn20search2turn20search14 | 高 |
| Zendesk AI | 客服工作流 | 工单系统、知识库、resolution loop | 高 | ROI 相对清晰，自动化优势明显 citeturn20search7turn20search11turn20search3 | 高 |
| Glean | 企业搜索 + 动作层 | 权限感知、连接器、actions | 中高 | 企业搜索的终局是“搜索 + 行动”而不是 RAG 壳子 citeturn21search1turn21search12turn21search15 | 高 |
| Harvey | 法务工作流 | 领域模板、流程、合规与事务上下文 | 中高 | 垂直 AI 的优质样本，但仍需警惕通用模型挤压 citeturn21search0turn21search8turn21news38 | 高 |
| Hebbia | 高风险知识工作 | 私有复杂数据、多代理研究、可回溯引用 | 中高 | 更像“高价值研究工作台”，不是一般问答机器人 citeturn21search6turn21search10turn21search13 | 中高 |
| NVIDIA Physical AI stack | Physical AI 平台 | 仿真、世界模型、芯片、生态 | 高 | 目前 Physical AI 的基础设施龙头样本 citeturn37view1turn37view0turn34search8 | 高 |
| Tesla Robotaxi / FSD / Optimus | 自动驾驶 / 机器人 | 车队、数据、控制栈、资本 | 中 | 战略意义大，商业成熟度仍未完全兑现 citeturn35news34turn35search13 | 中高 |
| Waymo | 自动驾驶 | 长期运营数据、车队、监管经验 | 高 | 当前商业闭环证据比 Tesla 更强 citeturn35search15turn35search0turn35search3 | 高 |
| Figure + BMW | 工业人形机器人 | 工厂场景、动作数据、集成能力 | 中 | 是人形机器人里少数更接近量产验证的案例 citeturn17search10turn17search0 | 中高 |
| DJI Enterprise / Dock | 无人机 / 低空自动化 | 硬件、飞控、行业方案、运维 | 高 | 是最被低估的成熟 Physical AI 样本之一 citeturn17search2turn17search8turn17search5 | 高 |
| Boston Dynamics Stretch + DHL | 仓储物流 | 可靠性、售后、场景标准化 | 高 | 窄场景、高 ROI 的代表 citeturn17search6turn17search3turn17search9 | 高 |
| Agility Digit + GXO | 仓储物流 | 运营数据、持续部署、机器人云平台 | 中高 | 比“酷炫 demo”更有商业意味 citeturn18search5turn18search0 | 高 |
| Unitree | 机器人硬件 | 成本与出货速度 | 中 | 有流量与量，但 B2B ROI 仍需更多公开数据 citeturn17search1turn17search4 | 中 |
| 智元机器人 | 中国具身智能 | 量产与项目落地信号 | 中 | 高潜力，需继续验证订单质量与维保效率 citeturn18search1turn18search3 | 中低 |
| 银河通用 | 中国具身智能 | 仿真到抓取的闭环叙事 | 中 | 技术故事强，商业验证需继续追踪 citeturn18search2turn18search9 | 中低 |
| Meta Ray-Ban / Orion | AI wearables / spatial | 终端入口、可穿戴上下文 | 中 | 更像“下一代入口层”，不是强 Physical AI 执行闭环 citeturn38view4turn16search6 | 中高 |

对未来三年的判断，可以压缩成四条。第一，**大厂会继续收缩重复、弱差异、弱留存的独立 AI App，但会继续加码入口、平台、企业连接、端侧与 agentic workflows。** 第二，**创业公司的机会不会消失，但会从“做一个聊天壳子”转向“占住一个控制点、拿住一类高价值任务、沉淀一套可复用动作系统”。** 第三，**ToB AI 会越来越像“软件产品 + 咨询部署 + 成本治理 + 评估体系”的复合产业，而不是传统 SaaS 的轻模式。** 第四，**Physical AI 会持续升温，但成熟赛道会优先出现在工业、物流、无人机、自动驾驶与智能基础设施，而不是最受媒体关注的家庭人形机器人。** citeturn23news36turn19search13turn20search6turn21search15turn17search3turn18search0turn35search15

如果把“最危险的方向”说得更具体，排在前面的通常是：**无入口的 C 端通用 AI、没有动作层的纯 RAG、强依赖人工配置的伪 Agent 平台、被当成营销功能售卖的 AI 硬件，以及只靠视频演示融资的人形机器人项目。** 与之相对，**最值得长期研究的五个 Physical AI 细分方向**，我建议是：工业制造自动化、仓储物流机器人、无人机与低空巡检、自动驾驶/Robotaxi、智能基础设施与固定感知系统。它们共同特征是：任务边界更清楚、ROI 更可算、部署频率更高、数据回流更持续。citeturn17search6turn17search3turn18search0turn17search2turn17search8turn35search15turn36search1

后续研究清单也应尽量“指标化”。建议长期跟踪的公司包括：OpenAI、Anthropic、Microsoft、Google、Apple、NVIDIA、ByteDance、Alibaba、Tencent、Baidu、Salesforce、ServiceNow、Glean、Harvey、DJI、Waymo、Tesla、Figure、Boston Dynamics、Agility、Unitree、智元、银河通用。建议跟踪的指标包括：**AI 收入占比、企业付费席位、任务完成量而非仅 token 量、单位客户毛利、人工接管率、动作成功率、边缘/云推理比例、部署周期、设备 uptime、售后密度、安全事件率、仿真数据与真实数据比值。** 这些指标比“装机量”“下载量”“融资额”更接近真实经营质量。citeturn19search13turn20search2turn21search15turn35search0turn17search3turn18search0

可执行的最小实验，我建议从五个方向入手。做一个**带权限和审计的企业知识动作台**，验证“答问题”到“完成动作”的差异；做一个**代码仓库 AI 审查与修复工作流**，跑通评估、回滚和成本限制；做一个**低时延端侧多模态 demo**，验证什么任务必须下沉到设备；做一个**仿真环境中的简单 VLA/控制实验**，例如 Isaac 或 MuJoCo 下的取放任务；做一个**真实业务 ROI 仪表盘**，把 AI 产出映射到工单解决率、合同周转时间、开发周期或巡检替代率上。只有进入这些实验，很多“泡沫”与“机会”才会在你的案例库里变成可反复检验的判断。citeturn21search15turn20search6turn37view5turn37view0

下面给出两份可以直接放进长期研究手册的判断清单。

**AI 应用项目判断清单**

| 判断项 | 通过标准 | 红旗信号 |
|---|---|---|
| 是否高频 | 周/日常复用明显 | 低频偶发需求 |
| 是否高价值 | 节省时间/降低风险/直接增收 | 只有“看起来方便” |
| 是否可验证 | 有明确正确性或业务结果指标 | 只能主观觉得好用 |
| 是否有付费意愿 | 已有预算科目或强 ROI | 只能靠免费拉新 |
| 是否有入口 | 内嵌现有工作台、OS、搜索、IDE、CRM 等 | 完全从零获客 |
| 是否有数据壁垒 | 数据独占、持续更新、有标签、有权限 | 只是公开资料堆叠 |
| 是否有工作流壁垒 | 能触发动作、审批、回滚、审计 | 只能聊，不能执行 |
| 是否有成本控制 | 小模型优先、缓存、批量、限流、观测 | 每次都上最贵模型 |
| 是否会项目制 | >70% 能靠产品内核和配置完成 | 每个客户都要重做 |
| 是否能沉淀产品资产 | 每次交付都会反哺模板、动作、评估、知识包 | 维护债务持续累积 |

这张清单本质上对应前文的公开产品路线：成熟产品几乎都在强化入口、动作层、权限、审计和成本治理，而不是单纯改善对话效果。citeturn20search1turn21search15turn20search6turn21search8

**物理 AI 项目判断清单**

| 判断项 | 通过标准 | 红旗信号 |
|---|---|---|
| 是否解决真实物理世界问题 | 有明确作业替代或效率提升 | 只是展示酷炫动作 |
| 是否比纯软件更必要 | 必须感知并执行现实动作 | 软件方案已足够 |
| 是否必须依赖硬件 | 硬件是能力核心而非营销壳 | 只是附会“设备”概念 |
| 是否有高频使用场景 | 日常/班次级/周期性任务 | 一年用几次 |
| 是否有明确付费方 | 工厂、仓库、运维、车队、医院等 | 付费主体模糊 |
| 是否能量化 ROI | 人工替代、产线效率、事故减少可量化 | 只能讲愿景 |
| 是否有真实数据闭环 | 设备运行数据持续回流训练 | 只能采集 demo 数据 |
| 是否有传感器/执行器壁垒 | 方案依赖真实硬件与控制 | 只靠通用零部件拼装 |
| 是否有端侧推理需求 | 时延/断网/隐私要求明确 | 云端即可完全代替 |
| 是否有安全与可靠性验证 | 有测试、容错、人工接管、责任边界 | 只展示最好情况 |
| 是否能规模化生产与维护 | 供应链、备件、维保可复制 | 一次性交付模式 |
| 是否依赖复杂交付 | 尽量少场景特化 | 每个现场都重做 |
| 是否只是 Demo 很酷 | 场景边界与价值明确 | 视频传播强于运营数据 |
| 是否存在监管/责任风险 | 合规路径清楚 | 责任主体不清 |
| 是否能形成长期数据和场景壁垒 | 运维与数据可复利 | 永远停留在单次项目 |

这张清单的核心就是把“热闹的机器人叙事”与“有经营质量的 Physical AI 项目”分开。它和 DJI、Boston Dynamics、Agility、Waymo、Apollo Go 这些案例的共同经验一致：只有当部署、维护和数据回流进入产品体系，Physical AI 才从资本故事变成产业能力。citeturn17search8turn17search6turn18search0turn35search15turn36search1

最后给出一个研究结论置信度表，方便你后续迭代这份手册：

| 置信度 | 结论 |
|---|---|
| 高 | AI 应用不是整体破裂，而是低壁垒、弱闭环、弱付费、无入口产品在出清；行业正在从“聊天工具”转向“平台、入口、工作流、执行系统”。 citeturn27search3turn23news36turn28search6turn20search6turn21search15 |
| 高 | 垂直工作流控制点应单独看，比泛泛“垂直数据”更能解释长期价值。 citeturn21search15turn21search8turn20search6turn20search7 |
| 高 | Physical AI 应单独列为第五方向，而不是简单并入“硬件 + AI 绑定”。 citeturn37view2turn37view0turn37view4 |
| 中 | 未来三年，Physical AI 的商业闭环会先在工业、物流、无人机、自动驾驶和智能基础设施里跑出来，而不是家庭人形机器人。 citeturn17search6turn17search8turn18search0turn35search15turn36search1 |
| 中 | 代码 Agent、法律 AI、客服 AI 会成为最先形成“高价值工作流控制点”的软件 AI 赛道。 citeturn20search1turn21search8turn20search7turn25news21 |
| 低到中 | 字节“砍掉 30% AI 项目”“80 亿推理成本为营收 2.3 倍”“3 个千万 DAU 产品全失败”这些说法，目前都缺少足够公开证据。 citeturn39view1turn39view0turn41search1turn41search0 |
| 低到中 | 孙宇晨关于 Physical AI 的细分方向流传版本，存在明显二手加工成分，需继续追查更完整原始材料。 citeturn14search0turn11search2turn11search14turn11search18 |

综合而言，你的初始直觉里有三点是对的：**其一，AI 应用层确实在出清，但不是整体坍塌；其二，ToB AI 很容易退化成项目制；其三，硬件与真实世界执行正在成为更重要的长期方向。** 但也有两点需要修正：**第一，不应把“泡沫破裂”理解成所有应用没有价值，而应理解成价值在重新分层；第二，Physical AI 不是天然优于软件 AI，它只是把难题从 token 成本换成了更重的工程、交付和安全问题。** 对长期研究者来说，最重要的不是选一个口号站队，而是把每一个判断转成：可跟踪公司的动作、可量化的指标、可重复的案例字段、可执行的最小实验。这样，研究手册才会从“观点集合”变成“判断系统”。 citeturn33search0turn21search15turn37view2turn17search3turn18search0