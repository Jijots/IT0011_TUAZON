fname = input("Enter your 1st name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

fullname = fname + " " + lname

greet = """Hello, {}! Welcome. You are {} years old."""

print("")
print("Full name: ", fullname)
print("Sliced name: ", fullname[0:3])
print("Greeting message: ", greet.format(fullname, age))