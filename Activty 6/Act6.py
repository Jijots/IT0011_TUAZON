class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = self.validate_price(price)

    def validate_price(self, price):
        try:
            price = float(price)
            if price < 0:
                raise ValueError("Price must be a positive number.")
            return price
        except ValueError:
            raise ValueError("Invalid price. Please enter a numeric value.")

    def __str__(self):
        return f"ID: {self.item_id} | Name: {self.name} | Description: {self.description} | Price: P{self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}
        self.next_id = 1

    def add_item(self):
        try:
            name = input("Enter item name: ").strip()
            if not name:
                raise ValueError("Item name cannot be empty.")

            description = input("Enter item description: ").strip()
            price = input("Enter item price: ").strip()

            item = Item(self.next_id, name, description, price)
            self.items[self.next_id] = item
            self.next_id += 1
            print("Item added successfully!\n")

        except ValueError as e:
            print(f"Error: {e}")

    def view_items(self):
        if not self.items:
            print("No items available.\n")
            return

        print("\nItem List:")
        for item in self.items.values():
            print(item)
        print()

    def update_item(self):
        try:
            item_id = int(input("Enter item ID to update: "))
            if item_id not in self.items:
                raise ValueError("Item ID not found.")

            name = input("Enter new name (leave blank to keep current): ").strip()
            description = input("Enter new description (leave blank to keep current): ").strip()
            price = input("Enter new price (leave blank to keep current): ").strip()

            item = self.items[item_id]
            if name:
                item.name = name
            if description:
                item.description = description
            if price:
                item.price = item.validate_price(price)

            print("Item updated successfully!\n")

        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self):
        try:
            item_id = int(input("Enter item ID to delete: "))
            if item_id not in self.items:
                raise ValueError("Item ID not found.")

            del self.items[item_id]
            print("Item deleted successfully!\n")

        except ValueError as e:
            print(f"Error: {e}")

    def menu(self):
        while True:
            print("Item Management Menu:")
            print("1. Add Item")
            print("2. View Items")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.view_items()
            elif choice == "3":
                self.update_item()
            elif choice == "4":
                self.delete_item()
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    manager = ItemManager()
    manager.menu()
