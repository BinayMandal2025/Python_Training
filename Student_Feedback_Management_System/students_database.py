
from dastabaseconnection import get_connection, connect, disconnect

class IntegrityError(Exception):
    pass

class Students_Database:
    
    def create_students_table(self):
        try:
            #print("Database: create students table")
            conn = get_connection()
            cursor = conn.cursor()
            query = """CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(200)
            )"""
            cursor.execute(query)
            #print(f"students table created !!")
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)

