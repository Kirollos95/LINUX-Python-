import math
#Printing Program Title
print("Scientific/Programmer/Basic Calculator")

while True:
    #Mode Choose Menu For User
    print("\nSelect an operation:")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Programmer Calculator")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Basic Calculator
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        #Selecting Basic Operations
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter the operation (1-4): ")

        result = 0
        #Switching Between Chosen Operation
        if operation == '1':
            result = num1 + num2
        elif operation == '2':
            result = num1 - num2
        elif operation == '3':
            result = num1 * num2
        elif operation == '4':
            result = num1 / num2
        else:
            print("Invalid operation!")

        print("Result:", result)

    elif choice == '2':
        # Scientific Calculator
        num = float(input("Enter a number: "))

        #Selecting Scientific Operations
        print("Select a scientific operation:")
        print("1. Square root")
        print("2. Logarithm (base 10)")
        print("3. Sine")
        print("4. Cosine")
        print("5. Tangent")

        operation = input("Enter the operation (1-5): ")

        result = 0

        #Switching Between Chosen Operation
        if operation == '1':
            result = math.sqrt(num)
        elif operation == '2':
            result = math.log10(num)
        elif operation == '3':
            result = math.sin(num)
        elif operation == '4':
            result = math.cos(num)
        elif operation == '5':
            result = math.tan(num)
        else:
            print("Invalid operation!")

        print("Result:", result)

    elif choice == '3':
        # Programmer Calculator
        num = input("Enter a number: ")

        #Selecting Programing Operations
        print("Select a programmer operation:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Decimal to Hexadecimal")
        print("4. Hexadecimal to Decimal")

        operation = input("Enter the operation (1-2): ")

        result = 0

        #Switching Between Chosen Operation
        if operation == '1':
            result = int(str(num), 2)
        elif operation == '2':
            result = bin(num)[2:]
        elif operation == '3':
            result = hex(num)
        elif operation == '4':
            result =int(str(num),16)
        else:
            print("Invalid operation!")

        print("Result:", result)

    elif choice == '4':
        # Exiting the calculator
        print("Exiting the calculator...")
        break

    else:
        print("Invalid choice!")
