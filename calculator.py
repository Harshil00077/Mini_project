#! /usr/bin/python3

import math

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def square_root(a):
    if a >= 0:
        return a**0.5
    else:
        return "Can't take square root of negative number"

def factorial(a):
    a = float(input("Enter The Number: "))
    if a >= 0:
        return math.factorial(int(a))
    else:
        return "Factorial of negative numbers is not defined."

def natural_logarithm(a):
    a = float(input("Enter First Number: "))
    if a > 0:
        return math.log(a)
    else:
        return "Cannot take log of negative or zero"

def power(a,b):
    return a**b

def main():

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
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result:", addition(a,b))
        elif ch == '2':
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result:", subtraction(a,b))
        elif ch == '3':
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result:", multiplication(a,b))
        elif ch == '4':
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result:", division(a,b))
        elif ch == '5':
            a = float(input("Enter The Number: "))
            print("Result:", square_root(a))
        elif ch == '6':
            a = float(input("Enter The Number: "))
            print("Result:", factorial(a))
        elif ch == '7':
            a = float(input("Enter The Number: "))
            print("Result:", natural_logarithm(a))
        elif ch == '8':
            a = float(input("Enter The Base for power: "))
            b = float(input("Enter Power of Number You Want: "))
            print("Result:", power(a,b))
        else:
            print("Exiting")
            break
if __name__ == "__main__":
    main()
