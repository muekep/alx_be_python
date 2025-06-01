try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print('Invalid input. Please enter whole number')
    exit()
print(f"\nMultiplication Table for {number}:")

for i in range(1,11):
    result = number * i
    print(f"{number} * {i} = {result}")
