# try:
#     a = int(input("Enter a number: "))
#     result = 10 / a
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")

import pdb
def add(a,b):
    pdb.set_trace()
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = add(a, b)
print("The sum is:", result)