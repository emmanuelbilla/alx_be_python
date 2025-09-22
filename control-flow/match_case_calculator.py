num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
    
    case "-":
        result = num1 - num2
    
    case "*":
        result = num1 * num2
    
    case "/":
        if num2 == 0:
            print("Can't divide by zero")
        else:
            result = num1 / num2
    case _:
        print("Invalid entry")
print("The result is " + str(result))