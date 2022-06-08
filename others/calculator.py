#calculator functions below

from cgi import print_form
from turtle import goto


def add(a, b):
    return "The sum is {}".format(a + b)
 
def subtract(a, b):
    return "Subtracting {} from {} gives {}".format(b, a, a - b)


def multiply(a, b):
    return "The product of {} and {} is: {}".format(a, b, a * b)


def divide(a, b):
    return "The quotient of {} and {} ({}/{}) is: {}".format(a, b, a, b, a / b)


print("If operation is addition write 1")
print("If operation is subtraction write 2")
print("If operation is multiplication write 3")
print("If operation is division write 4")

operation = input("Enter operation: ")
if operation not in ['1', '2', '3', '4']:
    print("Invalid expression leaving now 🙅‍♂️🙅‍♂️🙅‍♂️🙅‍♂️🙅‍♂️")
    exit()
firstNumber = int(input("Enter first number: "))
lastNumber = int(input("Enter last number: "))
if operation == "1":
    print(add(firstNumber, lastNumber))
elif operation == "2":
    print(subtract(firstNumber, lastNumber))
elif operation == "3":
    print(multiply(firstNumber, lastNumber))
elif operation == "4":
    print(divide(firstNumber, lastNumber))
else:
    print("Invalid operation entered. Try again")
