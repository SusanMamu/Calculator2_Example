def perform_operation(operation, num1, num2):
    if operation == 'addition':
        return num1 + num2
    elif operation == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("Division is not possible by zero")
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'subtraction':
        return num1 - num2


    else:
        print("No option chosen!")


operations = ["addition", "division", "multiplication", "division"]
print("Welcome!Available operations:")

for op in operations:
    print(op)

operation = input("Welcome!What would you like to do?")

if operation in operations:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = perform_operation(operation, num1, num2)
    print("Result:", result)

else:
    print("No valid operation chosen!Exit")
