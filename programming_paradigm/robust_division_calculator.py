def safe_divide(numerator, denominator):
    try:
        # Attempt to convert both inputs to float
        num1 = float(numerator)
        num2 = float(denominator)
    except ValueError:
        # Catch ValueError if conversion fails (non-numeric input)
        return "Error: Please enter numeric values only."

    try:
        # Attempt to perform division
        result = num1 / num2
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        # Catch ZeroDivisionError if denominator is zero
        return "Error: Cannot divide by zero." 
