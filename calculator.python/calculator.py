def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the simple calculator!")
    
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    if choice == '1':
        result = add(num1, num2)
        operation = "addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "division"
    else:
        result = "Invalid input"
        operation = None

    if operation:
        print(f"The result of the {operation} of {num1} and {num2} is: {result}")
    else:
        print(result)

if _name_ == "_main_":
    calculator()