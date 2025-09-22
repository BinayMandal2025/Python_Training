
from dastabaseconnection import get_connection, connect, disconnect

class Courses_Database:
 
    def create_course_table(self):
        #print("Database: create course table")
        conn = get_connection()
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS courses (
        course_id INT AUTO_INCREMENT PRIMARY KEY,
        course_name VARCHAR(200),
        faculty_name VARCHAR(100)
        )"""
        cursor.execute(query)
        cursor.close()
        conn.close()

   