import os

while True:
    print("Enter your choice:")
    print("Enter 1 to add record")
    print("Enter 2 to for further operation")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            choice = str(input("Enter student record as (Name, Roll, Marks): "))
            # Create a file named students.txt.
            with open('C:/RDT/Python/Data Types/file/students.txt','a') as f:
            #Write details of students (Name, Roll Number, Marks) into the file.
                f.write(f"{choice}\n")
        case _:
            break

if os.path.exists('C:/RDT/Python/Data Types/file/students.txt') == False:
    print("Student.txt file does not exist")
else:

    #Read the content of students.txt and display it on the screen.
    with open('C:/RDT/Python/Data Types/file/students.txt','r') as f:
        line = f.readlines()
        print(line)

    #Rename the file from students.txt to student_records.txt
    os.rename("C:/RDT/Python/Data Types/file/students.txt", "C:/RDT/Python/Data Types/file/student_records.txt")

    # Create a directory called SchoolData.    
    os.mkdir("C:/RDT/Python/Data Types/file/SchoolData")

    #Move the renamed file student_records.txt into this directory.
    os.replace("C:/RDT/Python/Data Types/file/student_records.txt", "C:/RDT/Python/Data Types/file/SchoolData/student_records.txt")

    #List all files present in SchoolData to confirm the file is inside.
    file_list = os.listdir("C:/RDT/Python/Data Types/file/SchoolData")
    print(file_list)

    #Delete the file student_records.txt from inside the directory.
    os.remove("C:/RDT/Python/Data Types/file/SchoolData/student_records.txt")

    #delete the SchoolData directory
    os.rmdir("C:/RDT/Python/Data Types/file/SchoolData")

