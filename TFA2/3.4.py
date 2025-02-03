try:
    with open("students.txt", "r") as file:
        content = file.read()
        print("Student Information:")
        print(content)
except FileNotFoundError:
    print("The file 'students.txt' does not exist.")