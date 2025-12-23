

## 🧱 安装方式
[![Trust Score](https://archestra.ai/mcp-catalog/api/badge/quality/tradercjz/dolphindb-mcp-server)](https://archestra.ai/mcp-catalog/tradercjz__dolphindb-mcp-server)

### ✅ 方法一：使用 `uvx`（推荐）

通过 `uvx` 安装并运行：

```bash
uvx install dolphindb-mcp-server
```

安装完成后，直接运行：
```bash
uvx dolphindb-mcp-server
```
> 📌 **注意**：`uvx` 安装方式需要通过 `uv.pack` 构建并上传到 Universe。如果你尚未上传，请参考 `uv` 文档进行打包与发布。

### ✅ 方法二：从 PyPI 安装

```bash
pip install dolphindb-mcp-server
```
安装后运行：
```bash
dolphindb-mcp-server
```

### ✅ 方法三：本地构建 & 安装

```bash
git clone https://github.com/your-org/dolphindb-mcp-server.git
cd dolphindb-mcp-server

# 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate

# 构建并安装
pip install build
python -m build
pip install dist/*.whl
```
安装后运行：
```bash
dolphindb-mcp-server
```

## 🧪 测试运行

运行后你可以直接使用工具，例如：

```bash
dolphindb-mcp-server
```

或（如果是 `uvx` 安装）：

```bash
uvx dolphindb-mcp-server
```
好的，这是转换后的 Markdown 版本：

好的，这是转换后的 Markdown 版本：

---

## 🚀 使用方法

1.  **配置环境变量（可选）**

    你可以通过 `.env` 文件或系统环境变量配置 DolphinDB 的连接信息：

    ```env
    DDB_HOST=127.0.0.1
    DDB_PORT=8848
    DDB_USER=admin
    DDB_PASSWD=123456
    ```

    也可以不设置，系统将使用默认值。

2.  **启动服务**

    ```bash
    dolphindb-mcp-server
    ```

    该命令会启动 MCP 插件服务，供外部调用。

3.  **FastMCP Agent 使用示例**

    启动后，你的工具将通过 FastMCP 对外暴露以下函数接口：

    *   `list_dbs()`
    *   `list_tbs(dbName: str)`
    *   `query_table_diskusage(database: str, tableName: str)`
    *   `query_dolphindb(script: str)`

    可通过 MCP 前端界面或对接 LLM 工具链来进行访问。
