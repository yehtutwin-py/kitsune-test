def addition(num1, num2):
    return round(num1 + num2, 2)
def subtraction(num1, num2):
    return round(num1 - num2, 2)
def multiplication(num1, num2):
    return round(num1 * num2, 2)
def division(num1, num2):
    if num2 != 0:
        return round(num1 / num2, 2)
    else:
        return "Error: Cannot divide by zero"
while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    user_choice = input("Choose an option(1-5): ")
    if user_choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = addition(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    elif user_choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = subtraction(num1, num2)
        print(f"The difference of {num1} and {num2} is {result}")
    elif user_choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiplication(num1, num2)
        print(f"The product of {num1} and {num2} is {result}")
    elif user_choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = division(num1, num2)
        print(f"The division of {num1} and {num2} is {result}")
    elif user_choice == "5":
        print("Thank you for using the Simple Calculator. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option (1-5).")