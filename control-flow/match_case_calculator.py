num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")
operation = input('Choose the operation (+, -, *, /):')
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    print("Invalid number input. Please enter a valid numerical values.")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1*num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1/num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")
exit()    
