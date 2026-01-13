from calculadora import *

def calculate(num1, num2, operation) -> int:
    if operation == "add":
        return suma(num1,num2)


if __name__ == '__main__':
    num1 = input("Select first parameter")
    operation = input("Select operation")
    num2 = input("Select second parameter")

    calculate(num1, num2, operation)