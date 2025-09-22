
from dastabaseconnection import get_connection, connect, disconnect

class Admins_Database:
   
    def create_admins_table(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS admins (
        admin_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100),
        password VARCHAR(100)
        )"""
        cursor.execute(query)
        cursor.close()
        conn.close()
    