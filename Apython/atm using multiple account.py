# Simple ATM System with Multiple Accounts

accounts = {
    "1001": {"pin": "1234", "balance": 5000},
    "1002": {"pin": "5678", "balance": 3000},
    "1003": {"pin": "0000", "balance": 10000}
}

def atm_menu(account):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance:", accounts[account]["balance"])

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            accounts[account]["balance"] += amount
            print("Deposit successful.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= accounts[account]["balance"]:
                accounts[account]["balance"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")

        elif choice == "4":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")

while True:
    print("\n--- Welcome to ATM ---")
    acc_no = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print("Login successful.")
        atm_menu(acc_no)
    else:
        print("Invalid account or PIN.")

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        print("Thank you for using ATM.")
        break
