def calculator(operation, num1, num2):
    if operation == "1":
        return round(num1 + num2, 2)
    elif operation == "2":
        return round(num1 - num2, 2)
    elif operation == "3":
        return round(num1 * num2, 2)
    elif operation == "4":
        if num2 != 0:
            return round(num1 / num2, 2)
        else:
            return "Error: Divide by zero."
    else:
        return "Invalid operation. Please choose a number between 1 and 4."
    
while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    user_choice = input("Choose an option(1-5): ")
    if user_choice == "5":
        print("Thank you for using the Simple Calculator. Goodbye!")
        break
    elif user_choice in ["1", "2", "3", "4"]:
        num1 = round(float(input("Enter the first number: ")), 2)
        num2 = round(float(input("Enter the second number: ")), 2)
        result = calculator(user_choice, num1, num2)
        print(f"The result is: {result}")
    else:
        print("Invalid option. Please choose a valid option (1-5).")