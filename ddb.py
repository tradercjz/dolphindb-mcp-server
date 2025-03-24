import dolphindb as ddb
from typing import Any, Tuple

class DatabaseSession:
    """数据库会话管理器"""
    def __init__(self, host: str, port: int, user: str, passwd: str, 
                 keep_alive_time: int = 3600, reconnect: bool = True, logger=None):
        self.host = host 
        self.port = port
        self.user = user 
        self.passwd = passwd
        self.keep_alive_time = keep_alive_time
        self.reconnect = reconnect
        self.session = ddb.session()
        self.logger = logger

    def __enter__(self):
        self.session.connect(
            self.host, 
            int(self.port), 
            self.user, 
            self.passwd,
            keepAliveTime=self.keep_alive_time, 
            reconnect=self.reconnect
        )
        return self 

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
    
    def execute(self, script: str) -> Tuple[bool, Any]:
        """执行DolphinDB脚本并返回结果或错误"""
        try:
            result = self.session.run(script)
            return True, result
        except Exception as e:
            return False, str(e)
