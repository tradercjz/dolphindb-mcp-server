

# Claude Code 接入 DolphinDB MCP Server 完整配置指南

本指南将帮助你在 **Claude Code** (Anthropic 官方 CLI) 中集成 **DolphinDB MCP Server**，实现通过 AI 直接查询、分析和操作 DolphinDB 数据库。

## 1. 环境准备

确保你的系统中已安装以下工具：
* **uv**: 高性能 Python 包管理器（推荐用于处理依赖）。安装：`pip install uv`
* **Claude Code**: 已全局安装（`npm install -g @anthropic-ai/claude-code`）。
* **DolphinDB Server**: 确保服务已启动且网络可达。

---

## 2. 下载并配置项目

首先，克隆源码并设置连接参数。

```bash
# 1. 克隆仓库
git clone https://github.com/tradercjz/dolphindb-mcp-server.git
cd dolphindb-mcp-server

# 2. 创建 .env 配置文件
# 如果目录下没有 .env，请手动创建一个
touch .env
```

在 `.env` 文件中填写你的 DolphinDB 连接信息（请根据实际情况修改）：
```ini
DDB_HOST=127.0.0.1
DDB_PORT=8848
DDB_USER=admin
DDB_PASSWD=123456
```

---

## 3. 在 Claude Code 中添加 MCP Server (关键步骤)

为确保 Claude 能正确读取 `.env` 配置并识别 Python 模块，**请务必按照以下顺序执行**：

### 第一步：进入项目根目录
打开终端，切换到你克隆项目的绝对路径：
```bash
cd /你的实际路径/dolphindb-mcp-server
```

### 第二步：执行添加命令
在项目根目录下，执行以下命令将 Server 注册到 Claude：

```bash
claude mcp add dolphindb -- \
  uv run --with fastmcp --with dolphindb --with python-dotenv \
  python -m dolphindb_mcp_server.server
```

> **注意：** > * 使用 `python -m` 模式可以避免 `ImportError`（相对导入报错）。
> * `uv run` 会自动在当前目录下寻找 `.env` 并加载环境变量。

---

## 4. 验证连接状态

添加完成后，运行以下命令检查：
```bash
claude mcp list
```

* **理想状态**：显示 `dolphindb: ... - ✓ Connected`。
* **如果显示 Failed**：请检查第一步中的 `cd` 路径是否正确，以及 `.env` 中的账号密码是否能正常登录 DolphinDB。

---

## 5. 开始使用

启动 Claude Code 进入交互模式：
```bash
claude
```

**你可以尝试以下指令：**
* "列出 DolphinDB 中当前所有的数据库和表。"
* "查询 `quotes` 表中最近 5 条记录。"
* "请帮我写一个 DolphinDB 脚本，计算某只股票的分钟级成交量加权平均价 (VWAP)。"



**这份文档现在逻辑闭环了。需要我再帮你写一个一键安装并配置的 Shell 脚本吗？**
