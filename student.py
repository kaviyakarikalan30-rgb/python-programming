n = int(input("How many students?"))

students ={}
for i in range(n):
    name = input(f"Enter name of student {i+1}:")
    mark = int(input(f"enter marks of {name}:"))
    students[name]=mark
    print("\n dictionary:", students)
    total_marks = sum(students.values())
    average_marks = total_marks /n
    print("Average marks:", average_marks)

    highest_marks = max(students.values())
    print("heights marks:", highest_marks)

    top_students = [name for name, marks in students.items() if mark == highest_marks]
    print("Top student(s):", top_students)