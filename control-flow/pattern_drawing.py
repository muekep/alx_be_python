while True:
    try:
<<<<<<< HEAD
        size_str = input("Enter the size of the pattern: ")
        size = int(size_str)
=======
        size = int(input("Enter the size of the pattern: "))
>>>>>>> b3ed7a0359b02bb440f061a6044cfbc091245d55

        if size <= 0:
            print("Please enter a positive integer.")
        else:
            break # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print(f"\nHere is a square pattern of size {size}:\n")

# Outer loop for rows
for _ in range(size):
    # Inner loop for columns
    for _ in range(size):
        # Print an asterisk followed by a space, without a new line
        print("* ", end="")
    # After each row, print a new line
<<<<<<< HEAD
    print()
=======
    print()
>>>>>>> b3ed7a0359b02bb440f061a6044cfbc091245d55
