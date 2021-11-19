#!/usr/bin/python3
# Source code for finding factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n >= 1:
            fact = fact * n
            n = n - 1
        return fact
print(factorial(5))
