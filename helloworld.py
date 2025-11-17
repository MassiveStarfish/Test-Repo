print("hello world")
def add_two_numbers(a, b):
    return a + b

def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def subtract_two_numbers(a, b):
    return a - b

def multiply_two_numbers(a, b):
    return a * b

if __name__ == "__main__":
    operation = input("Would you like to add, subtract, divide or multiply? (Type 'add', 'subtract', 'divide', or 'multiply'): ").lower()
    
    while operation not in ['add', 'divide', 'subtract', 'multiply']:
        operation = input("Invalid choice. Please type 'add', 'subtract', 'divide' or 'multiply': ").lower()
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    try:
        if operation == 'add':
            result = add_two_numbers(num1, num2)
            print(f"The sum of {num1} and {num2} is {result}")
        elif operation == 'subtract':
            result = subtract_two_numbers(num1, num2)
            print(f"The result of {num1} minus {num2} is {result}")
        elif operation == 'multiply':
            result = multiply_two_numbers(num1, num2)
            print(f"The result of {num1} times {num2} is {result}")
        else:  # divide
            result = divide_two_numbers(num1, num2)
            print(f"The result of {num1} divided by {num2} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
