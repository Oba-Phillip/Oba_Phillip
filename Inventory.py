def get_initial_inventory():
    inventory = {}
    print("Enter your initial inventory items.")
    print("Type 'done' when finished.\n")
    
    while True:
        item = input("Enter item name (or 'done' to finish): ").strip().lower()
        if item == 'done':
            break
        if item == '':
            print("Item name can't be empty.")
            continue
        
        if item in inventory:
            print(f"{item.title()} already added.")
            continue
        
        try:
            qty = int(input(f"Enter quantity for {item.title()}: "))
            if qty < 0:
                print("Quantity cannot be negative.")
                continue
            inventory[item] = qty
        except ValueError:
            print("Please enter a valid number for quantity.")
    
    return inventory

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")
    for item, qty in inventory.items():
        print(f"{item.title()}: {qty}")

def update_inventory(inventory):
    item = input("Enter item name to update: ").strip().lower()
    if item in inventory:
        try:
            qty = int(input(f"Enter new quantity for {item.title()}: "))
            if qty < 0:
                print("Quantity cannot be negative.")
                return
            inventory[item] = qty
            print(f"Updated {item.title()} to {qty}.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"{item.title()} not found in inventory.")

def add_item(inventory):
    item = input("Enter new item name: ").strip().lower()
    if item in inventory:
        print(f"{item.title()} already exists.")
        return
    if item == '':
        print("Item name cannot be empty.")
        return
    try:
        qty = int(input(f"Enter quantity for {item.title()}: "))
        if qty < 0:
            print("Quantity cannot be negative.")
            return
        inventory[item] = qty
        print(f"Added {item.title()} with quantity {qty}.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    inventory = get_initial_inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Update Item Quantity")
        print("3. Add New Item")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            update_inventory(inventory)
        elif choice == '3':
            add_item(inventory)
        elif choice == '4':
            print("Exiting Inventory Management. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    main()
