from sys import path
from os import system
from datetime import datetime
clear=lambda:system("cls")
students=[]
grades=[]
courses=[]
students_graduated=[]
from json import load
try:
    with open(path[0]+"/active_students.json","r") as active_students:
     students=load(active_students)
except(FileNotFoundError):
    students=[]
try:
    with open(path[0]+"/graduated_students.json","r") as graduated_students:
     students_graduated=load(graduated_students)
except(FileNotFoundError):
    students_graduated=[]
def validate_codemeli(codemeli):
    if len(codemeli)!=10:
        return False
    for student in students:
        if student["code_meli"]==codemeli:
            return False
    return True
def validate_studentcode(studentcode):
    for student in students:
        if student["student_code"]==studentcode:
            return False
    return True
def add_student():
    clear()
    student={}
    student["first_name"]=input("Enter your fisrt name: ")
    student["last_name"]=input("Enter your last name: ")
    if not student["first_name"].isalpha() or not student["last_name"].isalpha():
        input("\n First name or Last name is Wrong !")
        return False
    date_str=input("Enter your birthdate(yyyy/mm/dd)(such as 1999/2/5): ")
    date=datetime.strptime(date_str,'%Y/%m/%d')
    student["birthday"]=date.isoformat()
    student["code_meli"]=input("Enter your codemeli: ")
    if not validate_codemeli(student["code_meli"]):
        print("\nCodemeli Must be a 10 unique numbers !")
        return False
    while True:
        try:
            student["student_code"]=int(input("Enter your student's code: "))
            if not validate_studentcode(student["student_code"]):
                print("\nStudentcode Must be aunique numbers !")
                return False
            break
        except(ValueError):
            print("\nStudent's code must be a number !\n")
    courses_input=input("Enter your courses name(separated by spaces): ")
    student["courses"]=courses_input.split()
    courses=student["courses"]
    grades_input=input("Enter your grades (separated by spaces): ")
    grades_str=grades_input.split()
    student["grades"]=[float(i) for i in grades_str]
    grades=student["grades"]
    if not len(grades)==len(courses):
        input("\n Numbers of grades should math the numbers of courses !")
        return False
    students.append(student)
    input("\nThe students has been successfully added to database !")
def list_student()   :
    clear()
    print("\nActive students")
    print(40*"=","\n")
    for student in students:
        print("First_Name:",student["first_name"])
        print("Last_Name :",student["last_name"])
        print("Birthdate :",student["birthday"])
        def calculate_age(birth_date):
            today = datetime.today()
            age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            return age
        date_str=student["birthday"]
        date=datetime.strptime(date_str,'%Y-%m-%dT%H:%M:%S')
        age = calculate_age(date)
        print("Age: ",age)
        print("Codemeli :",student["code_meli"])
        print("courses :",student["courses"])
        print("grades :",student["grades"])
        grades_input=student["grades"]
        grades=[float(i) for i in grades_input]
        grades.sort(reverse=True)
        print("highest grade: ",grades[0])
        grades.sort()
        print("lowest grade is: ",grades[0])
        mean=sum(grades)/len(grades)
        print("the mean of the grades is: ",mean)
        print("----------------------------------------")
    print("\nGraduted students")
    print(40*"=","\n")
    for student in students_graduated:
        print("First_Name:",student["first_name"])
        print("Last_Name :",student["last_name"])
        print("Birthdate :",student["birthday"])
        def calculate_age(birth_date):
            today = datetime.today()
            age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            return age
        date_str=student["birthday"]
        date=datetime.strptime(date_str,'%Y-%m-%dT%H:%M:%S')
        age = calculate_age(date)
        print("Age: ",age)
        print("Codemeli :",student["code_meli"])
        print("courses :",student["courses"])
        print("grades :",student["grades"])
        grades_input=student["grades"]
        grades=[float(i) for i in grades_input]
        grades.sort(reverse=True)
        print("highest grade: ",grades[0])
        grades.sort()
        print("lowest grade is: ",grades[0])
        mean=sum(grades)/len(grades)
        print("the mean of the grades is: ",mean)
        print("----------------------------------------")
    input("\nPress Enter to return to menu ...")
def find_student():
    clear()
    codemeli=input("\nEnter codemeli to find your student: ")
    for student in students:
            if  codemeli==student["code_meli"]:
                print("First_Name:",student["first_name"])
                print("Last_Name :",student["last_name"])
                print("Birthdate :",student["birthday"])
                def calculate_age(birth_date):
                    today = datetime.today()
                    age = today.year - birth_date.year
                    if (today.month, today.day) < (birth_date.month, birth_date.day):
                        age -= 1
                    return age
                date_str=student["birthday"]
                date=datetime.strptime(date_str,'%Y-%m-%dT%H:%M:%S')
                age = calculate_age(date)
                print("Age: ",age)
                print("Codemeli :",student["code_meli"])
                print("courses :",student["courses"])
                grades_input=student["grades"]
                grades=[float(i) for i in grades_input]
                grades.sort(reverse=True)
                print("highest grade: ",grades[0])
                grades.sort()
                print("lowest grade is: ",grades[0])
                mean=sum(grades)/len(grades)
                print("the mean of the grades is: ",mean)
                print("This student is active !")
                print("----------------------------------------")
                break
    else:
        input("\nThis Student does not exit in database !")
                
    for student in students_graduated:
            if  codemeli==student["code_meli"]:
                    print("First_Name:",student["first_name"])
                    print("Last_Name :",student["last_name"])
                    print("Birthdate :",student["birthday"])
                    print("Codemeli :",student["code_meli"])
                    print("courses :",student["courses"])
                    grades_input=student["grades"]
                    grades=[float(i) for i in grades_input]
                    grades.sort(reverse=True)
                    print("highest grade: ",grades[0])
                    grades.sort()
                    print("lowest grade is: ",grades[0])
                    mean=sum(grades)/len(grades)
                    print("the mean of the grades is: ",mean)
                    print("This student is graduated !")
                    print("----------------------------------------")
                    break
    else:
        input("\nThis Student does not exit in database !")
                
    input("\nPress Enter to return to menu ...")
def delete_student():
    clear()
    code_meli=input("Please Enter your students codemeli: ")
    for student in students:
        if student["code_meli"] == code_meli:
            action = input("Do you want to transfer this student to graduated students (t) or delete them (d)? ")
            if action == "d":
                students.remove(student)
                print("\nThe student has been deleted successfully!")
            else:
                students.remove(student)
                students_graduated.append(student)
                print("\n Student has been transferd successfulyy !")
            break
    else:
        input("\nThis student does not exist in active students! Press Enter to continue...")
def change_courses():
    clear()
    n=input("Enter your students codemeli: ")
    for student in students:
        if n==student["code_meli"]:
            courses=student["courses"]
            grades_input=student["grades"]
            grades=[float(i) for i in grades_input]
            print(courses)
            e=input("if you want to add a course pleas enter C and if you want to remove a course press R(Note=your courses are numbered between 0-n)?: ").upper()
            if e=="R":
                while True:
                 try:
                  index=int(input("enter your course number: "))
                  break
                 except(ValueError):
                  print("\n You have to remove the course by its number !")
                courses.pop(index)
                grades.pop(index)
                student["grades"]=grades
                input("\n  The Course has been removed successfully!")
                break       
            elif e=="C":
               nc=input("Enter your courses name(separated by spaces): ")
               courses_input1=nc
               courses_list1=courses_input1.split()
               for i1 in courses_list1:
                    course=str(i1)
                    courses.append(course)
               grades_input=input("Enter your grades (separated by spaces): ")
               grades_str=grades_input.split()
               grades=[float(i) for i in grades_str]
               student["grades"].extend(grades)
               input("\n  The Course has been added successfully!")
               break   
    else:
        input("\nThis student does not exist in active students! Press Enter to continue...")
def save_students():
    from json import dump
    with open(path[0]+"/active_students.json","w") as active_student:
        dump(students,active_student,indent=4)
    with open(path[0]+"/graduated_students.json","w") as graduated_students:
        dump(students_graduated,graduated_students,indent=4)
    input("\n The students have been saved successfully!")
    

