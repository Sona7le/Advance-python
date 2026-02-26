account = {
    "balance": 0.0,
    "history": []
}

SECRET_PIN = "9939"

def authenticate():
    tries = 3
    while tries:
        user_pin = input("Enter PIN: ")
        if user_pin == SECRET_PIN:
            print("Access granted.\n")
            return True
        tries -= 1
        print(f"Incorrect PIN. Remaining tries: {tries}")
    print("Too many failed attempts. Access denied.")
    return False


def add_money():
    try:
        amt = float(input("Amount to deposit: "))
        if amt > 0:
            account["balance"] += amt
            account["history"].append(f"Deposit -> {amt}")
            print("Amount added successfully.")
        else:
            print("Enter a valid amount.")
    except:
        print("Invalid input.")


def take_money():
    try:
        amt = float(input("Amount to withdraw: "))
        if amt <= 0:
            print("Enter a valid amount.")
        elif amt > account["balance"]:
            print("Not enough funds.")
        else:
            account["balance"] -= amt
            account["history"].append(f"Withdraw -> {amt}")
            print("Please collect your cash.")
    except:
        print("Invalid input.")


def show_balance():
    print(f"Available Balance: {account['balance']}")


def show_history():
    print("\n--- Transaction Log ---")
    if account["history"]:
        for record in account["history"]:
            print(record)
    else:
        print("No activity yet.")


def options():
    print("""
==== ATM MENU ====
1 -> Deposit Money
2 -> Withdraw Money
3 -> Balance Inquiry
4 -> Transaction Log
5 -> Quit
""")
    return input("Select option: ")


if authenticate():
    while True:
        opt = options()

        if opt == '1':
            add_money()
        elif opt == '2':
            take_money()
        elif opt == '3':
            show_balance()
        elif opt == '4':
            show_history()
        elif opt == '5':
            print("Session ended. Goodbye!")
            break
        else:
            print("Invalid selection.")
