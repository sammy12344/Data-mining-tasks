# Calculator

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("Error: You can't divide by zero!")
    return x / y


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Select an operation: "))


while choice in (1, 2, 3, 4):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
        break
    elif choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
        break
    elif choice == 3:
        print(f"{num1} x {num2} = {multiply(num1, num2)}")
        break
    elif choice == 4:
        print(f"{num1} - {num2} = {divide(num1, num2)}")
        break
else:
    print("Invalid input")

