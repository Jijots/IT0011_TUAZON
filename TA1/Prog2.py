input_string = input("Enter a string with digits: ")

sum_of_digits = 0

for char in input_string:
    if char.isdigit():
        sum_of_digits += int(char)

print("Sum of digits:", sum_of_digits)
