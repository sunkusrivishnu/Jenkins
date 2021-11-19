def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n >= 1:
            fact = fact * n
            n = n - 1
        return fact

print factorial(0)
print factorial(1)
print factorial(5)
print factorial(6)
