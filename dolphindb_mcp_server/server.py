from fastmcp import FastMCP
from typing import Any
from .ddb import DatabaseSession
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
def list_dbs() -> Any:
    """
    查看 DolphinDB 中有哪些库
    """
    with DatabaseSession(**DDB_CONFIG) as db:
        return db.execute("getClusterDFSDatabases()")
    
@mcp.tool()
def list_tbs(dbName: str) -> Any:
    """
    查看 DolphinDB中，某个分布式库下面有哪些表
    :param dbName: DolphinDB的库名称，通常是dfs://开头的
    :return: 分布式库包含的表
    """
    with DatabaseSession(**DDB_CONFIG) as db:
        return db.execute(f"getTables(database(\"{dbName}\"))")
    
    
@mcp.tool()
def query_table_diskusage(database: str, tableName: str) -> Any:
    """
    查看DolphinDB中，某个库表，其磁盘空间占用
    :param database: DolphinDB的库名称，通常是dfs://开头的
    :param tableName: DolphinDB的表名称
    :return 磁盘占用
    """
    with DatabaseSession(**DDB_CONFIG) as db:
        return db.execute(f"use ops; getTableDiskUsage(\"{database}\", \"{tableName}\", byNode=false)")

@mcp.tool()
def query_dolphindb(script: str) -> Any:
    """
    在 DolphinDB 执行查询
    :param script: 要执行的 DolphinDB 脚本
    :return: 查询结果
    """
    with DatabaseSession(**DDB_CONFIG) as db:
        return db.execute(script)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
