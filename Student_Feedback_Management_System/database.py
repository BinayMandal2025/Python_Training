
from dastabaseconnection import get_connection, connect, disconnect
from logger import CustomLogger, LoggingType

log = CustomLogger("database")

class Database:
    def create_DB(self):
        conn = connect()
        cursor = conn.cursor()
        query = """CREATE DATABASE IF NOT EXISTS feedback_system;
        )"""
        cursor.execute(query)
        log.write_log(f"feedback_system database created", LoggingType.info)
        
        cursor.close()
        conn.close()


   