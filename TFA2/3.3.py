fname = input("Enter your 1st name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")
conNum = input("Enter your contact number: ")
course = input("Enter your course: ")

formattedInfo = f"Last name: {lname}, First Name: {fname}, Age: {age}, Contact Number: {conNum}, Course: {course}\n"

with open("students.txt", "a") as file:
    file.write(formattedInfo)

print("Student information has been saved to students.txt")