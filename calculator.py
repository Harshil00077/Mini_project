#! /usr/bin/python3

import math

def addition():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    return a + b

def subtraction():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    return a - b

def multiplication():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    return a * b

def division():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def square_root():
    a = float(input("Enter The Number: "))
    if a >= 0:
        return a**0.5
    else:
        return "Can't take square root of negative number"

def factorial():
    a = float(input("Enter The Number: "))
    if a >= 0:
        return math.factorial(int(a))
    else:
        return "Factorial of negative numbers is not defined."

def natural_logarithm():
    a = float(input("Enter First Number: "))
    if a > 0:
        return math.log(a)
    else:
        return "Cannot take log of negative or zero"

def power():
    a = float(input("Enter The Base for power: "))
    b = float(input("Enter Power of Number You Want: "))
    return a**b

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Factorial")
    print("7. Natural Logarithm")
    print("8. Power")
    print("9- Exit")

    ch = input("Enter the Choice: ")

    if ch == '1':
        print("Result:", addition())
    elif ch == '2':
        print("Result:", subtraction())
    elif ch == '3':
        print("Result:", multiplication())
    elif ch == '4':
        print("Result:", division())
    elif ch == '5':
        print("Result:", square_root())
    elif ch == '6':
        print("Result:", factorial())
    elif ch == '7':
        print("Result:", natural_logarithm())
    elif ch == '8':
        print("Result:", power())
    else:
        print("Exiting")
        break
