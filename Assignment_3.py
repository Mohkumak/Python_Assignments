 # Task 1: Calculate Factorial Using a Function

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
number = 5
output = factorial(number)
print(f"factorial of {number} is {output}")

# Task 2: Using the Math Module for Calculations

user = int(input("enter a number: "))
import math
print(f"sqaure root: {math.sqrt(user)}")
print(f"logarithm: {math.log(user)}")
print(f"sine: {math.sin(user)}")


