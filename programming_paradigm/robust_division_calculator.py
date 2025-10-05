def safe_divide(numerator, denominator):
    try:
         # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator/ denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # Prints error message to output for zero division
        return "Error: Cannot divide by zero." 
        
    except ValueError:
        #Prints error message for non-numeric inputs
        return "Error: Please enter numeric values only."