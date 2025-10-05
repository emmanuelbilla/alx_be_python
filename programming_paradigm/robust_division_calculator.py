def safe_divide(numerator, denominator):
    try:
         # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator/ denominator
        return result
    except ZeroDivisionError:
        # Prints error message for zero division
        print("Error: Cannot divide by zero.") 
        
    except ValueError:
        # Prints error message for non-numeric inputs
        print("Error: Please enter numeric values only.")
        