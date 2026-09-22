def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=  i
    return fact

n = int(input("Enter n value :"))
print("Factorial is :",factorial(n))
# print("Factorial is :",factorial(5))