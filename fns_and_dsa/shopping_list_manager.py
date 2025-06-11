def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Shopping List Manager ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    print("----------------------------")

def add_item(shopping_list: list):
    """Prompts the user for an item and adds it to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item: # Ensure item is not empty
        shopping_list.append(item)
        print(f"'{item}' added to the list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list: list):
    """Prompts the user for an item and removes it from the shopping list."""
    item = input("Enter the item to remove: ").strip()
    if item: # Ensure item is not empty
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the list.")
        else:
            print(f"'{item}' not found in the list.")
    else:
        print("Item name cannot be empty.")

def view_list(shopping_list: list):
    """Displays all items currently in the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\n--- Your Shopping List ---")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        print("--------------------------")

def main():
    """Main function to run the shopping list manager application."""
    shopping_list = []
    running = True

    while running:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        match choice:
            case '1':
                add_item(shopping_list)
            case '2':
                remove_item(shopping_list)
            case '3':
                view_list(shopping_list)
            case '4':
                running = False
                print("Exiting Shopping List Manager. Goodbye!")
            case _: # Handles any other input
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

