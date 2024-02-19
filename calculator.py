#! /usr/bin/python3

import math


def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

while(True):
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
        res = a + b
    elif ch == '2':
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        res = a - b
    elif ch == '3':
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        res = a * b
    elif ch == '4':
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        if b != 0:
            res = a / b
        else:
            res = "Cannot divide by zero"
    elif ch == '5':
        a = float(input("Enter The Number: "))
        if a>=0:
            res = a**0.5
        else:
            res = "can't take square root of negative number"
    elif ch == '6':
        a = float(input("Enter The Number: "))
        if a>=0:
            res = fact(a)
        else:
            res = "Factorial of negative numbers is not defined."
    elif ch == '7':
        a = float(input("Enter First Number: "))
        if a > 0:
            res = math.log(a)
        else:
            res = "Cannot take log of negative or zero"
    elif ch == '8':
        a = float(input("Enter The Base for power: "))
        b = float(input("Enter Power of Number You Want: "))
        res = a**b
    else:
        res = "Exiting"
    
    if res!="Exiting":
        print("Result:", res)
    else:
        break
