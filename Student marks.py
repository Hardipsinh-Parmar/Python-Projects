student_marks = {"rahul":80,
                 "hardip":70,
                 "bob":60}

while True:
 print("********MENU********")
 print("1 to display all student's marks")
 print("2 to search student's marks")
 print("3 to add a new student's marks")
 print("4 to update student's marks")
 print("5 to delete student")
 print("6 to exit")

 result = input("Enter your choice: ")
 if result == "6":
     break
 elif result == "1":
     for key, value in student_marks.items():
         print(f"{key}: {value}",end=" ")
         print()
 elif result == "2":
     name = input("Enter name of the student: ").lower()
     if name in student_marks:
      print(f"{name}: {student_marks[name]}")
     else:
      print("Student not found.")
 elif result == "3":
   name = input("Enter name of the student: ").lower()
   if name in student_marks:
          print("Student already exists")
   else:
    marks = int(input("Enter marks: "))
    student_marks.update({name : marks})
 elif result == "4":
     name = input("Enter name of the student: ").lower()
     if name in student_marks:
      marks = int(input("Enter marks: "))
      student_marks.update({name : marks})
      print(f"{name}: {marks}")
 elif result == "5":
    name = input("Enter name of the student: ").lower()
    if name in student_marks:
     student_marks.pop(name)
    else :
         print("Student not found.")
 else:
     print("Invalid input")
