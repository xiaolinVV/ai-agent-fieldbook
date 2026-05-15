# RAGFlow 官方 Docker 部署记录

日期：2026-05-13（服务器时区：Asia/Shanghai）

## 结论

本机适合按 RAGFlow 官方仓库的 Docker Compose 标准方式部署 RAGFlow。

- 已部署版本：`infiniflow/ragflow:v0.25.2`
- 代码目录：`/home/fjhc/dev/ragflow`
- Compose 目录：`/home/fjhc/dev/ragflow/docker`
- Web 访问地址：`http://192.168.10.131:18080`
- 监听策略：按当前需求暴露到所有网卡，即 `0.0.0.0` / `[::]`，支持局域网访问。
- 当前未启用内置/本地 embedding 服务；`v0.22.0` 起官方镜像不再内置 embedding 模型。

不要把这套部署理解成生产安全配置。当前仍保留官方默认密码，适合可信内网实验；如果要给更多人长期使用，先改密码和防火墙策略。

## 本机环境评估

官方 `v0.25.2` README 的最低要求：

| 项目 | 官方最低要求 | 本机情况 | 判断 |
| --- | --- | --- | --- |
| CPU | `>= 4 cores` | 64 cores | 满足 |
| RAM | `>= 16 GB` | 125 GiB | 满足 |
| Disk | `>= 50 GB` | 部署后仍有约 796 GiB 可用 | 满足 |
| Docker | `>= 24.0.0` | `29.3.1` | 满足 |
| Docker Compose | `>= v2.26.1` | `v5.1.1` | 满足 |
| 架构 | 官方镜像仅支持 x86 | `x86_64` | 满足 |
| `vm.max_map_count` | `>= 262144` | `1048576` | 满足 |
| GPU | 可选 | 未检测到 NVIDIA GPU/runtime | 使用 CPU 部署 |
| gVisor / `runsc` | 仅代码执行沙箱需要 | 未安装 | 不影响基础 RAGFlow；代码执行沙箱暂不可用 |

核心判断：基础 RAGFlow 部署是真问题，值得做；为了“自带 embedding”降级到旧镜像不是好方案。旧镜像只是把模型塞进镜像，换来更大的镜像和更旧的系统版本，不值得。

## 版本选择

当前选择：

```bash
RAGFLOW_IMAGE=infiniflow/ragflow:v0.25.2
```

选择理由：

- `v0.25.2` 是实施时从官方仓库 tags 验证到的最新稳定发布 tag。
- 官方 README 默认示例也是 `v0.25.2`。
- `nightly` 是“最近测试过”的镜像，但不是稳定发布版；学习和内网实践没必要先吃这个风险。
- `v0.22.0` 起官方只发布不带 embedding 模型的 slim 形态镜像，并且不再追加 `-slim` 后缀。
- `v0.21.1` 这类老版本有带 embedding 的 full 镜像，但为了内置模型牺牲当前版本功能和维护路径，不划算。

后续 embedding 策略：

- 优先：在 RAGFlow Web UI 中配置外部 LLM/embedding provider，适合快速验证企业 RAG 流程。
- 如果要本机 embedding：启用官方 TEI profile。当前 `.env` 已保留：
  - `TEI_PORT=16380`
  - `TEI_MODEL=${TEI_MODEL:-Qwen/Qwen3-Embedding-0.6B}`
- TEI 模型资源差异：
  - `Qwen/Qwen3-Embedding-0.6B`：官方标注约需 25GB RAM/vRAM。
  - `BAAI/bge-m3`：官方标注约需 21GB RAM/vRAM。
  - `BAAI/bge-small-en-v1.5`：官方标注约需 1.2GB RAM/vRAM，适合先做轻量冒烟验证。

## 当前端口规划

为了避开本机已有服务，同时满足局域网访问，端口全部以 Docker 默认方式发布到所有网卡。

| 服务 | 宿主机端口 | 容器端口 | 用途 |
| --- | ---: | ---: | --- |
| RAGFlow Web | `18080` | `80` | 浏览器访问入口 |
| RAGFlow HTTPS | `18443` | `443` | HTTPS 入口，未额外配置证书 |
| RAGFlow API | `19380` | `9380` | 后端 HTTP API |
| RAGFlow Admin API | `19381` | `9381` | Admin 服务 |
| RAGFlow MCP | `19382` | `9382` | MCP 服务 |
| RAGFlow Go Admin | `19383` | `9383` | Go Admin |
| RAGFlow Go HTTP | `19384` | `9384` | Go HTTP |
| Elasticsearch | `1200` | `9200` | 搜索/索引服务 |
| MySQL | `15455` | `3306` | 元数据数据库 |
| Redis/Valkey | `16379` | `6379` | 缓存/队列 |
| MinIO API | `19000` | `9000` | 对象存储 API |
| MinIO Console | `19001` | `9001` | 对象存储控制台 |
| TEI | `16380` | `80` | 本地 embedding 服务，当前未启用 |

`.env` 中的关键配置：

```bash
ES_PORT=1200
MEM_LIMIT=17179869184
EXPOSE_MYSQL_PORT=15455
MINIO_CONSOLE_PORT=19001
MINIO_PORT=19000
REDIS_PORT=16379
SVR_WEB_HTTP_PORT=18080
SVR_WEB_HTTPS_PORT=18443
SVR_HTTP_PORT=19380
ADMIN_SVR_HTTP_PORT=19381
SVR_MCP_PORT=19382
GO_HTTP_PORT=19384
GO_ADMIN_PORT=19383
RAGFLOW_IMAGE=infiniflow/ragflow:v0.25.2
TEI_MODEL=${TEI_MODEL:-Qwen/Qwen3-Embedding-0.6B}
TEI_PORT=16380
```

## 实施步骤

拉取官方代码并固定 tag：

```bash
git clone --depth 1 --branch v0.25.2 https://github.com/infiniflow/ragflow.git /home/fjhc/dev/ragflow
```

修改配置：

```bash
cd /home/fjhc/dev/ragflow/docker
vim .env
```

至少确认：

```bash
RAGFLOW_IMAGE=infiniflow/ragflow:v0.25.2
MEM_LIMIT=17179869184
SVR_WEB_HTTP_PORT=18080
SVR_HTTP_PORT=19380
```

验证 Compose 配置：

```bash
cd /home/fjhc/dev/ragflow/docker
docker compose --env-file .env -f docker-compose.yml config --quiet
```

启动服务：

```bash
cd /home/fjhc/dev/ragflow/docker
docker compose --env-file .env -f docker-compose.yml up -d
```

查看状态：

```bash
docker compose --env-file .env -f docker-compose.yml ps
```

查看 RAGFlow 日志：

```bash
docker logs -f docker-ragflow-cpu-1
```

看到类似日志即可认为 RAGFlow 服务完成初始化：

```text
RAGFlow admin is ready
RAGFlow data sync is ready
RAGFlow ingestion is ready
RAGFlow server is ready
Running on http://0.0.0.0:9380
```

## 当前验证结果

容器状态：

```text
docker-es01-1          Up (healthy)   0.0.0.0:1200->9200
docker-minio-1         Up (healthy)   0.0.0.0:19000->9000, 0.0.0.0:19001->9001
docker-mysql-1         Up (healthy)   0.0.0.0:15455->3306
docker-redis-1         Up (healthy)   0.0.0.0:16379->6379
docker-ragflow-cpu-1   Up             0.0.0.0:18080->80, 0.0.0.0:19380->9380
```

Web 本机访问：

```bash
curl -sS -I --connect-timeout 5 http://127.0.0.1:18080
```

结果：

```text
HTTP/1.1 200 OK
Server: nginx/1.29.5
```

Web 通过局域网 IP 访问：

```bash
curl -sS -I --connect-timeout 5 http://192.168.10.131:18080
```

结果：

```text
HTTP/1.1 200 OK
Server: nginx/1.29.5
```

Elasticsearch 健康检查：

```bash
curl -sS -u elastic:infini_rag_flow http://127.0.0.1:1200/_cluster/health?pretty
```

关键结果：

```json
{
  "status": "green",
  "number_of_nodes": 1
}
```

Redis/Valkey 检查：

```bash
docker exec docker-redis-1 valkey-cli -a infini_rag_flow ping
```

结果：

```text
PONG
```

监听地址检查：

```bash
ss -ltnp
```

关键结果：`1200`、`15455`、`16379`、`18080`、`18443`、`19000`、`19001`、`19380`、`19381`、`19382`、`19383`、`19384` 均监听在 `0.0.0.0` 和 `[::]`。

说明：这证明服务没有被绑定到 `127.0.0.1`。真实局域网客户端访问还受宿主机防火墙、交换机/VLAN、路由策略影响；本次未修改防火墙。

## 日常维护命令

进入部署目录：

```bash
cd /home/fjhc/dev/ragflow/docker
```

查看服务：

```bash
docker compose --env-file .env -f docker-compose.yml ps
```

查看主服务日志：

```bash
docker logs -f docker-ragflow-cpu-1
```

查看全部服务日志：

```bash
docker compose --env-file .env -f docker-compose.yml logs -f
```

停止服务但保留数据：

```bash
docker compose --env-file .env -f docker-compose.yml down
```

重新启动：

```bash
docker compose --env-file .env -f docker-compose.yml up -d
```

拉取当前配置需要的镜像：

```bash
docker compose --env-file .env -f docker-compose.yml pull
```

检查数据卷：

```bash
docker volume ls
```

当前数据卷：

```text
docker_esdata01
docker_minio_data
docker_mysql_data
docker_redis_data
```

不要随手执行：

```bash
docker compose --env-file .env -f docker-compose.yml down -v
```

`-v` 会删除 Docker volumes，也就是 MySQL、MinIO、Redis、Elasticsearch 数据。这个命令不是“重启”，是“删库重来”。

## 备份与迁移

官方迁移脚本在：

```bash
/home/fjhc/dev/ragflow/docker/migration.sh
```

备份前先停止服务：

```bash
cd /home/fjhc/dev/ragflow
docker compose -f docker/docker-compose.yml down
```

执行备份：

```bash
bash docker/migration.sh backup
```

恢复：

```bash
bash docker/migration.sh restore
docker compose -f docker/docker-compose.yml up -d
```

如果使用本文当前端口配置，恢复后仍要检查 `docker/.env` 是否保留了本机端口规划。

## 升级策略

RAGFlow 官方要求升级时同时升级两件事：

1. 仓库代码
2. Docker 镜像 tag

升级到指定稳定版本的基本流程：

```bash
cd /home/fjhc/dev/ragflow
docker compose --env-file docker/.env -f docker/docker-compose.yml down
git fetch --tags
git checkout -f vX.Y.Z
vim docker/.env
docker compose --env-file docker/.env -f docker/docker-compose.yml pull
docker compose --env-file docker/.env -f docker/docker-compose.yml up -d
```

`.env` 中必须同步：

```bash
RAGFLOW_IMAGE=infiniflow/ragflow:vX.Y.Z
```

不要只改镜像、不切代码；也不要只切代码、不改镜像。入口脚本和配置模板可能随版本变化，不匹配就是给自己制造故障。

## 启用本地 TEI embedding

当前没有启用 TEI。后续如果要启用 CPU 版本地 embedding：

```bash
cd /home/fjhc/dev/ragflow/docker
vim .env
```

取消注释：

```bash
COMPOSE_PROFILES=${COMPOSE_PROFILES},tei-cpu
```

可按资源选择模型：

```bash
TEI_MODEL=${TEI_MODEL:-BAAI/bge-small-en-v1.5}
```

然后启动：

```bash
docker compose --env-file .env -f docker-compose.yml up -d
```

启用后检查：

```bash
docker compose --env-file .env -f docker-compose.yml ps
curl -sS http://127.0.0.1:16380/health
```

注意：embedding 模型一旦用于某个知识库并产生 chunks，后续切换 embedding 模型通常需要删除并重新解析该知识库的 chunks。不同 embedding 空间不能混用，这是 RAG 系统的基本约束，不是 RAGFlow 的特殊毛病。

## 安全注意事项

当前端口暴露到所有网卡，这是为了局域网访问，符合本次部署目标。但这也意味着局域网内其他机器可以探测这些服务。

上线给团队使用前至少做三件事：

1. 修改 `.env` 中 MySQL、Redis、MinIO、Elasticsearch 等默认密码。
2. 用防火墙只放行必要来源 IP 和必要端口，通常只需要开放 `18080`。
3. 不要把 `1200`、`15455`、`16379`、`19000`、`19001` 这类基础设施端口暴露到不可信网络。

本次未验证 `ufw`，因为普通用户执行 `ufw status` 需要 root 权限。

## 常见排查

检查 RAGFlow 是否启动完成：

```bash
docker logs docker-ragflow-cpu-1
```

检查 Web：

```bash
curl -sS -I http://127.0.0.1:18080
curl -sS -I http://192.168.10.131:18080
```

检查 ES：

```bash
curl -sS -u elastic:infini_rag_flow http://127.0.0.1:1200/_cluster/health?pretty
```

检查 Redis：

```bash
docker exec docker-redis-1 valkey-cli -a infini_rag_flow ping
```

检查端口是否监听到所有网卡：

```bash
ss -ltnp
```

如果局域网其他机器访问不了：

- 先在服务器上确认 `curl http://192.168.10.131:18080` 返回 `200 OK`。
- 再检查宿主机防火墙、云安全组、交换机/VLAN、客户端路由。
- 不要把服务改成 `127.0.0.1`，那会直接破坏局域网访问需求。

## 官方参考

- RAGFlow README `v0.25.2`：<https://github.com/infiniflow/ragflow/blob/v0.25.2/README.md>
- Docker 配置说明：<https://github.com/infiniflow/ragflow/blob/v0.25.2/docs/administrator/configurations/configurations.md>
- 升级说明：<https://github.com/infiniflow/ragflow/blob/v0.25.2/docs/administrator/upgrade_ragflow.mdx>
- 备份与迁移说明：<https://github.com/infiniflow/ragflow/blob/v0.25.2/docs/administrator/migration/backup_and_migration.md>
- 本地模型部署说明：<https://github.com/infiniflow/ragflow/blob/v0.25.2/docs/guides/models/deploy_local_llm.mdx>
