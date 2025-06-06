#Python Compound Interest Calculator
print("Welcome to Python Compound Interest Calculator")

P = int(input("Enter your Principal amount:" ))
r = float(input("Enter your annual interest rate:"))
n = int(input("Enter number of times interest is compounded per year:"))
t = int(input("Enter the number of years:"))
A = P * pow((1 + r / 100*n), n * t)
print(f"Final amount is :{A:.2f}")