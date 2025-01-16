def calculator():
    print("Welcome to the Simple Calculator!")
    print("You can perform the following operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ").strip()
        
        if operation == '+':
            result = num1 + num2
            print("Result = ",result)
        elif operation == '-':
            result = num1 - num2
            print("Result = ",result)
        elif operation == '*':
            result = num1 * num2
            print("Result = ",result)
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print("Result = ",result)
            else:
                print("\nDivision by zero is not allowed.....Please try again.....")
        else:
            print("\nInvalid operation...Please choose one of the following: +, -, *, or /")
    
    except ValueError:
        print("\nYou entered an invalid number. Please try again with valid numerical values...")

calculator()
