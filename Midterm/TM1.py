def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    with open(filename, 'r') as file:
        line_number = 1
        for line in file:
            numbers = line.strip().split(',')
            numbers = [int(num) for num in numbers]
            total = sum(numbers)

            if is_palindrome(total):
                result = "Palindrome"
            else:
                result = "Not a palindrome"

            print(f"Line {line_number}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
            line_number += 1

process_file("numbers.txt")