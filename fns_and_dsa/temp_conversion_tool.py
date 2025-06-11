CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
FREEZING_POINT_ADJUSTMENT = 32

def convert_to_celsius(fahrenheit: float) -> float:

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
  
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ").strip()
            temperature = float(temp_input) # Attempt to convert input to float
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            # Continue the loop to prompt again

    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if unit in ['C', 'F']:
            break # Exit loop if unit is valid
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Perform conversion based on unit
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    else: # unit == 'F'
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")

if __name__ == "__main__":
    main()
