import sys
sys.path.append(r"C:\Users\Binay.mandal\AppData\Local\Programs\Python\Python312\Lib\site-packages")

import mysql.connector

from logger import CustomLogger, LoggingType

log = CustomLogger("databaseconnection")

class DatabaseConnectionError:
     pass

 
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        database="feedback_system",
        user="root",
        password="kol@mind1"
    )
    return conn

def connect():
        try:
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kol@mind1"
            )
            return conn
 
        except Exception as e:
            print(e)
            log.write_log(f"Exception while connecting SQL", LoggingType.error)
            raise DatabaseConnectionError("Exception while connecting SQL")
 
def disconnect():
    try:
        print("Disconnect database")
    except Exception as e:
        print(e)
        log.write_log(f"Exception while disconnecting from database", LoggingType.error)

        raise DatabaseConnectionError("Exception while disconnecting from database" )