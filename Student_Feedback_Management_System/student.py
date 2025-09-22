import sys
sys.path.append(r"C:\Users\Binay.mandal\AppData\Local\Programs\Python\Python312\Lib\site-packages")
import mysql.connector
from mysql.connector import IntegrityError
from dastabaseconnection import get_connection, connect, disconnect
from logger import CustomLogger, LoggingType

log = CustomLogger("student")

# from mysql.connector import Error, errorcode
class DuplicateFeedbackError(Exception):
    pass

class Student:

    def register(self, name, email, password):
        ret = 0
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Insert into students (name,email,password) values(%s,%s,%s)"
            cursor.execute(query, (name,email,password))
            conn.commit()
            log.write_log(f"Student:{name} registered successfully", LoggingType.info)
        except mysql.connector.IntegrityError as e:
            ret = 1
            log.write_log(f"Student:{name} registered integrity error", LoggingType.error)
       
        except Exception as e:
            ret = 2
            log.write_log(f"Student:{name} register: general exception error", LoggingType.error)
            print(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            return ret

    def login(self, email, password):
        studentid = 0
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select student_id from students where email = %s and password = %s"
            cursor.execute(query, (email,password))
            result = cursor.fetchone()
            studentid = result[0]
            if result:
                log.write_log(f"Student log in successfully", LoggingType.info)

            else:
                log.write_log(f"Student log in: Invalid login credentials.", LoggingType.info)
          
        except Exception as e:
            print(e)
            log.write_log(f"Student log in: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return studentid

    def submit_feedback(self, feedback):
        ret = False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT feedback_id from feedback where student_id = %s and course_id = %s"
            cursor.execute(query, (feedback.student_id, feedback.course_id,))
            result = cursor.fetchone()
            if result:
                log.write_log(f"Duplicate feedback submission", LoggingType.info)
                raise DuplicateFeedbackError("Duplicate Feedback Error")
            else:
                query = "Insert into feedback (student_id,course_id,rating,comments) values(%s,%s,%s,%s)"
                cursor.execute(query, (feedback.student_id,feedback.course_id, feedback.rating, feedback.comments))
                conn.commit()
                
                log.write_log(f"Feedback submitted by {feedback.student_id} at timestamp", LoggingType.info)

                ret = True
          
        except Exception as e:
            print(e)
            log.write_log(f"Feedback submit: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            return ret
        

    def get_student_name(self, student_id):
        result = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select name from students where student_id = %s"
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()
            result1 = result[0]
            

            if result1:
                log.write_log(f"Student name retrive from student id", LoggingType.info)

            else:
                log.write_log(f"Wrong student name", LoggingType.info)

          
        except Exception as e:
            print(e)
            log.write_log(f"Feedback get student name: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return result1
