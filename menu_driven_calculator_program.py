while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    user_choice = input("Choose an option(1-5): ")
    # decimal 2 places
    if user_choice == "1":
        num1 = round(float(input("Enter the first number: ")), 2)
        num2 = round(float(input("Enter the second number: ")), 2)
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    elif user_choice == "2":
        num1 = round(float(input("Enter the first number: ")), 2)
        num2 = round(float(input("Enter the second number: ")), 2)
        result = num1 - num2
        print(f"The difference of {num1} and {num2} is {result}")
    elif user_choice == "3":
        num1 = round(float(input("Enter the first number: ")), 2)
        num2 = round(float(input("Enter the second number: ")), 2)
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}")
    elif user_choice == "4":
        num1 = round(float(input("Enter the first number: ")), 2)
        num2 = round(float(input("Enter the second number: ")), 2)
        if num2 != 0:
            result = round(num1 / num2, 2)
            print(f"The divison of {num1} and {num2} is {result}")
        else:
            print("Error: Cannot divide by zero")
    elif user_choice == "5":
        print("Thank you for using the Simple Calculator. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option (1-5).")