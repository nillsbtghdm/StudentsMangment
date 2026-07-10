import students_opertions as sp
import os
#---------------------------------------------
while True:
    print("\nWelcome To Sabetghadam's Institution!")
    print(40*"=")
    print("Press A to add a student")
    print("Press L to list all students")
    print("Press F to find a student")
    print("Press C to change courses")
    print("Press D to delete a student")
    print("Press S to save all students")
    print("Press Q to quit application")
    print(40*"=")
    choice=input("\nEnter your choice: ").upper()
    if  choice=="A":
        sp.add_student()
    elif choice=="L":
        sp.list_student()
    elif choice=="F":
        sp.find_student()
    elif choice=="D":
        sp.delete_student()
    elif choice=="S":
        sp.save_students()
    elif choice=="C":
        sp.change_courses()
    elif choice=="Q":
        break
    else:
        input("\nWronge Choice!")