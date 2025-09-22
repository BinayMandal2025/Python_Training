
from dastabaseconnection import get_connection, connect, disconnect

class Feedback_Database:
   
    def create_feedback_table(self):
        #print("Database: create feedback table")
        conn = get_connection()
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS feedback (
        feedback_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        course_id VARCHAR(100),
        rating INT,
        comments VARCHAR(300)
        )"""
        cursor.execute(query)
        cursor.close()
        conn.close()

    


