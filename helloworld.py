print("hello world")

print("i'm making a change")


=======
def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    operation = input("Would you like to add or divide? (Type 'add' or 'divide'): ").lower()
    
    while operation not in ['add', 'divide']:
        operation = input("Invalid choice. Please type 'add' or 'divide': ").lower()
    
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
        else:  # divide
            result = divide_two_numbers(num1, num2)
            print(f"The result of {num1} divided by {num2} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
>>>>>>> d0d51956c71f40153d37ded709ff9273bc06fe8a
