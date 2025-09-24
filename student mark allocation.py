# Program to store and display student details with 3 subjects and marks

# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
class_name = input("Enter class: ")

# Taking subject names and marks
subjects = {}
for i in range(1, 4):
    subject_name = input(f"Enter subject {i} name: ")
    marks = int(input(f"Enter marks for {subject_name}: "))
    subjects[subject_name] = marks

# Display student details
print("\n---- Student Details ----")
print("Name      :", name)
print("Roll No   :", roll_no)
print("Class     :", class_name)

print("\n---- Marks ----")
total = 0
for subject, mark in subjects.items():
    print(f"{subject}: {mark}")
    total += mark

percentage = total / 3
print("\nTotal Marks :", total)
print("Percentage  :", percentage, "%")