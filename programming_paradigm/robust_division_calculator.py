def safe_divide(numerator, denominator):
    try:
         # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator/ denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        # Prints error message to output for zero division
        print("Error: Cannot divide by zero.") 
        
    except ValueError:
        #Prints error message for non-numeric inputs
        print("Error: Please enter numeric values only.")