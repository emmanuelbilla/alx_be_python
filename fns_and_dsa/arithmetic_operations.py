def perform_operation(num1, num2, operation):
    match operation:
        case "+":
            result = num1 + num2
            return result

        case "-":
                result = num1 - num2
                return result

        case "*":
            result = num1 * num2
            return result

        case "/":
            if num2 == 0:
                print("Can't divide by zero")
            
            else:
                result = num1 / num2
                return result
        case _: 
            print("Invalid entry")
        
