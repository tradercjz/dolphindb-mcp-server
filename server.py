from fastmcp import FastMCP
from typing import Any
from ddb import DatabaseSession
from dotenv import load_dotenv
import os 

load_dotenv()

DDB_CONFIG = {
    "host": os.getenv("DDB_HOST", "127.0.0.1"),
    "port": os.getenv("DDB_PORT", "8848"),
    "user": os.getenv("DDB_USER", "admin"),
    "passwd": os.getenv("DDB_PASSWD", "123456")
}

mcp = FastMCP("dolphindb-mcp-server")

@mcp.tool()
def query_dolphindb(script: str) -> Any:
    """
    在 DolphinDB 执行查询
    :param script: 要执行的 DolphinDB 脚本
    :return: 查询结果
    """
    with DatabaseSession(**DDB_CONFIG) as db:
        return db.execute(script)
    
print("OKOKOKOKO")