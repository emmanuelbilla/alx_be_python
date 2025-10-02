def perform_operation( num1: float , num2: float, operation: str):
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
        
    try:
        print("The result is " + str(result))
    except UnboundLocalError:
        print("No result to show.")

perform_operation(1,3,"^")