from dastabaseconnection import get_connection, connect, disconnect
from logger import CustomLogger, LoggingType

log = CustomLogger("admin")

class Admin:
    def add_adminuser(slef):
        try:
            username = "admin"
            password = "root"
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select username from admins where username = %s and password = %s"
            cursor.execute(query, (username,password))
            result = cursor.fetchone()
            if result:
                log.write_log(f"Admin:{username}  already registered", LoggingType.info)

            else:
                query = "Insert into admins (username,password) values(%s,%s)"
                cursor.execute(query, (username,password))
                conn.commit()

          
        except Exception as e:
            print(e)
            log.write_log(f"Admin:{username} register: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def login(self, username, password):
        ret = False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select username from admins where username = %s and password = %s"
            cursor.execute(query, (username,password))
            result = cursor.fetchone()
            if result:
                log.write_log(f"Admin:{username} log in successful", LoggingType.info)
                ret = True
            else:
                log.write_log(f"Admin:Wrong username of password", LoggingType.error)

          
        except Exception as e:
            print(e)
            log.write_log(f"Admin:{username} log in: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            return ret

    def view_feedback(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select * from feedback"
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                log.write_log(f"Admin:: Feedback featch succeesful", LoggingType.info)

            else:
                log.write_log(f"Admin:: No feedback record found", LoggingType.info)



          
        except Exception as e:
            print(e)
            log.write_log(f"Admin:view feedback: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            return result
