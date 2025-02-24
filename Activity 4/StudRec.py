def save_record(record, filename):
    with open(filename, 'a') as file:
        file.write(record + '\n')
    print(f"Record saved successfully in {filename}.")

def show_records(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read().strip())
    except FileNotFoundError:
        print("No records found.")

def add_record(filename):
    stud_id = input("Enter Student ID: ")
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    cStanding = input("Enter Class Standing: ")
    majExam = input("Enter Major Exam Grade: ")
    record = f"Student ID: {stud_id}\nFull Name: {lname}, {fname}\nClass Standing: {cStanding}\nMajor Exam Score: {majExam}\n"
    save_record(record, filename)

filename = "records.txt"

while True:
    print("\nMenu:")
    print("1. Show Records")
    print("2. Add Record")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_records(filename)
    elif choice == "2":
        add_record(filename)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")
