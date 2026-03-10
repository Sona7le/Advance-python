# Simple CRM (Customer Relationship Manager)

customers = {}

# Add new customer
def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    status = input("Enter status (New/Interested/Closed): ")

    customers[name] = {
        "phone": phone,
        "email": email,
        "status": status,
        "communication": []
    }

    print("Customer added successfully!\n")


# Record communication with customer
def add_communication():
    name = input("Enter customer name: ")

    if name in customers:
        note = input("Enter communication note: ")
        customers[name]["communication"].append(note)
        print("Communication recorded!\n")
    else:
        print("Customer not found!\n")


# View customer details
def view_customer():
    name = input("Enter customer name: ")

    if name in customers:
        print("\nCustomer Information")
        print("Name:", name)
        print("Phone:", customers[name]["phone"])
        print("Email:", customers[name]["email"])
        print("Status:", customers[name]["status"])
        print("Communication Logs:", customers[name]["communication"])
        print()
    else:
        print("Customer not found!\n")


# Update customer status
def update_status():
    name = input("Enter customer name: ")

    if name in customers:
        new_status = input("Enter new status: ")
        customers[name]["status"] = new_status
        print("Status updated!\n")
    else:
        print("Customer not found!\n")


# Main menu
while True:
    print("---- CRM System ----")
    print("1. Add Customer")
    print("2. Record Communication")
    print("3. View Customer")
    print("4. Update Status")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_customer()

    elif choice == "2":
        add_communication()

    elif choice == "3":
        view_customer()

    elif choice == "4":
        update_status()

    elif choice == "5":
        print("Exiting CRM system")
        break

    else:
        print("Invalid choice\n")
