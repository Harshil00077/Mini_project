#! /usr/bin/python3

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
ch = input("Enter the Choice: ")

if ch == '1':
    res = a + b
elif ch == '2':
    res = a - b
elif ch == '3':
    res = a * b
elif ch == '4':
    if b != 0:
        res = a / b
    else:
        res = "Cannot divide by zero"
else:
    res = "Invalid Choice"

print("Result:", res)
