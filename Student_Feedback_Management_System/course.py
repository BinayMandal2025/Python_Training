from dastabaseconnection import get_connection, connect, disconnect
from logger import CustomLogger, LoggingType

log = CustomLogger("course")

class Courses:
    def add_courses(self, course_name, faculty_name):
        coursename = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select course_name from courses where course_name = %s and faculty_name = %s"
            cursor.execute(query, (course_name,faculty_name))
            result = cursor.fetchone()
            if result != None:
                coursename = result[0]

            if coursename == course_name:
                log.write_log(f"Course: Course and faculty alrady added, ignoring", LoggingType.info)

            else:
                query = "Insert into courses (course_name, faculty_name) values(%s,%s)"
                cursor.execute(query, (course_name, faculty_name))
                conn.commit()
                log.write_log(f"Course: Course and faculty added", LoggingType.info)
                
                

        except Exception as e:
            log.write_log(f"Course: add course: general exception error", LoggingType.error)
            print(e)
        finally:
            # if cursor:
            #     cursor.close()
            if conn:
                conn.close()

    def featch_courses(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select * from courses"
            cursor.execute(query)
            results = cursor.fetchall()
            name = [{'course_id': result[0], 'course_name': result[1]} for result in results]
            log.write_log(f"Course: course featch successful", LoggingType.info)

        except Exception as e:
            print(e)
            log.write_log(f"Course: course featch: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            return name
        
    def get_course_name(self, course_id):
        result = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "Select course_name from courses where course_id = %s"
            cursor.execute(query, (course_id,))
            result = cursor.fetchone()
            result1 = result[0]

            if result1:
                log.write_log(f"Course: Course name retrive", LoggingType.info)

            else:
                log.write_log(f"Course: Wrong course name", LoggingType.info)

          
        except Exception as e:
            print(e)
            log.write_log(f"Course: course name: general exception error", LoggingType.error)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return result1
