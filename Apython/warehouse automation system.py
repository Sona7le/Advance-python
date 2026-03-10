# Warehouse Management System using Class

class Warehouse:

    def __init__(self):
        # Dictionary to store goods
        self.goods = {}

    # Method to add goods
    def add_goods(self, name, quantity, price):
        if name in self.goods:
            self.goods[name]["quantity"] += quantity
        else:
            self.goods[name] = {"quantity": quantity, "price": price}
        print(f"{name} added/updated successfully.")

    # Method to check availability
    def check_availability(self, name):
        if name in self.goods:
            print(f"{name} is available.")
            print("Quantity:", self.goods[name]["quantity"])
        else:
            print(f"{name} is not available in warehouse.")

    # Method to check price
    def check_price(self, name):
        if name in self.goods:
            print(f"Price of {name} is ₹{self.goods[name]['price']}")
        else:
            print(f"{name} not found in warehouse.")

    # Method to display all goods
    def display_goods(self):
        if not self.goods:
            print("Warehouse is empty.")
        else:
            print("\n--- Warehouse Stock ---")
            for item in self.goods:
                print("Item:", item)
                print("Quantity:", self.goods[item]["quantity"])
                print("Price: ₹", self.goods[item]["price"])
                print("----------------------")


# Creating object
warehouse1 = Warehouse()

# Menu Driven Program
while True:
    print("\n1. Add Goods")
    print("2. Check Availability")
    print("3. Check Price")
    print("4. Display All Goods")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        warehouse1.add_goods(name, quantity, price)

    elif choice == "2":
        name = input("Enter item name to check: ")
        warehouse1.check_availability(name)

    elif choice == "3":
        name = input("Enter item name to check price: ")
        warehouse1.check_price(name)

    elif choice == "4":
        warehouse1.display_goods()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
