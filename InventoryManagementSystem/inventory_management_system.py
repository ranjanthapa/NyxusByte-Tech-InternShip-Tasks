import datetime
from abc import ABC, abstractmethod


class Inventory(ABC):
    @abstractmethod
    def add_items(self):
        pass

    @abstractmethod
    def update_item(self, name: str):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def remove_item(self, name: str):
        pass

    @abstractmethod
    def low_stock_report(self):
        pass

    def sort_inventory(self, inventory_list: list):
        inventory_list.sort(key=lambda inventory: inventory["price"], reverse=True)


class InventoryItem(Inventory):
    obj_count = 0
    inventory_list = []

    def __init__(self, name, price, quantity, category=None):
        InventoryItem.obj_count += 1
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def add_items(self):
        if self.is_numeric(self.price) and self.is_numeric(self.quantity):
            new_item = {
                "name": self.name,
                "price": self.price,
                "quantity": self.quantity,
                "category": self.category.split(' ')
            }
            self.inventory_list.append(new_item)
            print("added")

    @staticmethod
    def is_numeric(value):
        return isinstance(value, (int, float)) and value > 0

    def is_inventory_empty(self):
        if not self.inventory_list:
            return True

    def update_item(self, name):
        if self.is_inventory_empty():
            print("Inventory is empty")
        else:
            found = False
            print(self.inventory_list)
            for item in self.inventory_list:
                if item["name"] == name:
                    name = input("Update the item name or leave it to keep the same: ")
                    price = input("Update the item price or leave it to keep the same: ")
                    quantity = input("Update the item quantity or leave it to keep the same: ")
                    category = input("Update the item category: ")
                    if name or price or quantity or category:
                        if name:
                            item["name"] = name
                        if price:
                            try:
                                item["price"] = int(price)
                            except ValueError:
                                print("Price should be integer not alphabetic")
                        if quantity:
                            try:
                                item["quantity"] = int(quantity)
                            except ValueError:
                                print("Quantity should be integer not alphabetic")
                        if category:
                            item["category"] = category
                        print("Updated successfully")
                    else:
                        print("Nothing changed")
                    found = True
                    break

            if not found:
                print("Item with the name not found")

    def remove_item(self, name):
        if self.is_inventory_empty():
            print("Inventory list is empty")
        else:
            found_item = True
            try:
                confirm_delete = input("are you sure you want to remove y/n?").lower()
                if confirm_delete == "y":
                    for item in self.inventory_list:
                        if item["name"] == name:
                            self.inventory_list.remove(item)
                            found_item = True
                            break

                    if not found_item:
                        print("Item with the name doesn't exists")
            except ValueError:
                print("Confirm to delete if yes type 'y' else 'n'")

    def display(self):

        self.inventory_list.sort(key=lambda inventory: inventory["price"], reverse=True)
        for item in self.inventory_list:
            print(
                f"Item Name: {self.name} \nPrice: {item['price']} \nQuantity: {item['quantity']} \nCategory: {item['category']}\n"
            )

    def low_stock_report(self):
        low_stocks = [item for item in self.inventory_list if item['quantity'] < 10]
        if low_stocks:
            print("Lists of items with the low quantity")
            for low_stock in low_stocks:
                print(
                    f"Item Name: {low_stock['name']} \n Price: {low_stock['price']} \n Quantity: {low_stock['quantity']} \n "
                    f"Category: {low_stock['category']}")
        else:
            print("There are no stock with low quantity")


class Electronic(InventoryItem):
    class Electronic(InventoryItem):
        def __init__(self, name, price, quantity, category=None, added_date=""):
            self.added_date = added_date
            super().__init__(name, price, quantity, category=category)

    def add_items(self):
        if super().is_numeric(self.price) and super().is_numeric(self.quantity):
            new_item = {
                "name": self.name,
                "price": self.price,
                "quantity": self.quantity,
                "category": self.category,
                "added_date": datetime.datetime.now()
            }
            self.inventory_list.append(new_item)
            print("added")


def main():
    electronic_item = None
    exit_program = False
    print("\nChoose an action:")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Remove Item")
    print("4. Display Inventory")
    print("5. Low Stock Report")
    print("6. Exit")
    while not exit_program:
        user_choice = input("Enter your choice (1-6): ")

        if user_choice == '1':
            name = input("Enter the product name: ")
            price = float(input("Enter the price of product: "))
            quantity = int(input("Enter the product quantity: "))
            category = input("Enter the category of list: ")
            electronic_item = Electronic(name, price, quantity, category)
            electronic_item.add_items()
        elif user_choice == '2':
            name_to_update = input("Enter the name of the item to update: ")
            if electronic_item:
                electronic_item.update_item(name_to_update)
            else:
                print("No item to update. Please add an item first.")
        elif user_choice == '3':
            name_to_remove = input("Enter the name of the item to remove: ")
            if electronic_item:
                electronic_item.remove_item(name_to_remove)
            else:
                print("No item to remove. Please add an item first.")
        elif user_choice == '4':
            if electronic_item:
                electronic_item.display()
            else:
                print("No items to display. Please add an item first.")
        elif user_choice == '5':
            if electronic_item:
                electronic_item.low_stock_report()
            else:
                print("No items to generate a low stock report. Please add an item first.")
        elif user_choice == '6':
            exit_program = True
            print("Exiting the program.")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
