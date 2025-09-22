import sys
import os
sys.path.append(r"C:\Users\Binay.mandal\AppData\Local\Programs\Python\Python312\Lib\site-packages")
from database import Database
from students_database import Students_Database
from courses_database import Courses_Database
from feedback_database import Feedback_Database
from admins_database import Admins_Database
from admin import Admin
from course import Courses
from student import Student
from feedback import Feedback
from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory # type: ignore
from logger import CustomLogger, LoggingType

log = CustomLogger("main")
selected_student_id = 0
def create_db():
    db = Database()
    db.create_DB()

def create_tables():
    students_db = Students_Database()
    students_db.create_students_table()

    courses_db = Courses_Database()
    courses_db.create_course_table()

    feedback_db = Feedback_Database()
    feedback_db.create_feedback_table()

    admins_db = Admins_Database()
    admins_db.create_admins_table()

    admin= Admin()
    admin.add_adminuser()

    course = Courses()
    course.add_courses("Data Analyst", "Rajan Sharma")
    course.add_courses("AWS Services", "Chetan Khanna")
    course.add_courses("Gen AI", "Shekhar Patil")



app = Flask(__name__)
 
@app.route('/register',methods=['GET','POST'])
def form_register():
    if request.method == 'POST':
        log.write_log("Registering student user:", LoggingType.info)
        name = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        student = Student()
        ret = student.register(name, email, pwd)

        if ret == 0:
            log.write_log("Student registration successfully, redirecting login page", LoggingType.info)
            return redirect(url_for('form_login'))
        elif ret == 1:
            log.write_log("Student is already registered!!!", LoggingType.info)
            return f"{name}, Student is already registered !!!"
        else:
            return f"{name}, Your registration failed !!"
    return '''
        <form method="POST">
        <label for="username">Username:</label><br>
        <input type="text" name="username"><br>
        <label for="username">Email:</label><br>
        <input type="text" name="email"><br>
        <label for="username">Password:</label><br>
        <input type="text" name="password"><br><br>
        <input type="submit">
        </form>
'''

@app.route('/login',methods=['GET','POST'])
def form_login():
    if request.method == 'POST':
        log.write_log("Checking log in details:", LoggingType.info)
        email = request.form['email']
        pwd = request.form['password']
        student = Student()
        global selected_student_id
        selected_student_id = student.login(email, pwd)

        if selected_student_id:
            return redirect(url_for('form_submit_student_feedback'))
        
        log.write_log("Fail to login, please check username and password", LoggingType.error)
        return f"Hello, email or password or both wrong !!"
    return '''
        <form method="POST">
        <label for="username">Email:</label><br>
        <input type="text" name="email"><br>
        <label for="username">Password:</label><br>
        <input type="text" name="password"><br><br>
        <input type="submit">
        </form>
'''

@app.route('/submit_feedback',methods=['GET','POST'])
def form_submit_student_feedback():
    if request.method == 'POST':
        log.write_log("Submitting feedback...", LoggingType.info)
        global selected_student_id
        student_id = selected_student_id
        course_id = request.form.get('course_id')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        feedback = Feedback(student_id, course_id, rating, comments)
        student = Student()
        status = student.submit_feedback(feedback)
        if status == True:
            return "Feedback submitted successfully !!"
        
        log.write_log("Fail to submit feedback, please check", LoggingType.error)
        return "Fail to submit feedback, please check !!"
    
    courses = Courses()
    courses_list = courses.featch_courses()
    return render_template("feedback_submit.html", courses=courses_list)

@app.route('/admin/login',methods=['GET','POST'])
def form_admin_login():
    if request.method == 'POST':
        log.write_log("Verifying admin login details...", LoggingType.info)
        usr = request.form['username']
        pwd = request.form['password']
        admin_usr = Admin()
        status = admin_usr.login(usr, pwd)
        if status == True:
            log.write_log("Admin login successful", LoggingType.info)
            return redirect(url_for('form_admin_feedback'))
        else:
            log.write_log("Admin login fail", LoggingType.info)
            return "Invalid user name or password !!"
    return '''
        <form method="POST">
        <label for="username">User Name:</label><br>
        <input type="text" name="username"><br>
        <label for="username">Password:</label><br>
        <input type="text" name="password"><br><br>
        <input type="submit">
        </form>
'''

@app.route('/admin/feedback',methods=['GET','POST'])
def form_admin_feedback():
    if request.method == 'POST':
        data = request.form['email']
        pwd = request.form['password']
        return f"Hello {data} , your email is registered successfully !!"
    
    admin = Admin()
    feedback_lists = admin.view_feedback()
    name1 = []
    for feedback_list in feedback_lists:
        student = Student()
        name = student.get_student_name(feedback_list[1])
        course = Courses()
        course_name = course.get_course_name(feedback_list[2])
        localName = {'name': name, 'course_name': course_name, 'rating': feedback_list[3], "comment": feedback_list[4]}
        name1.append(localName)
    return render_template("feedback_view.html", feedback_list=name1)

# Route to send the file from C drive
@app.route('/download')
def download_file():
    file_path = r'C:\RDT\Python\logs\app.log'  # Raw string for Windows path
    if os.path.exists(file_path):
        log.write_log("Log downloaded", LoggingType.info)
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == "__main__":
    log.write_log("****************Log started******************", LoggingType.info)
    create_db()
    create_tables()
    app.run(debug=True,use_reloader=False)
    

       
