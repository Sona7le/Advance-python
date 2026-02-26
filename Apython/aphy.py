bal = 0
trans = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice = "))

    if choice == 1:
        amt = int(input("Enter the amount you want to deposit = "))
        bal += amt
        trans.append(f"Deposit: {amt}")
        print("Amount deposited successfully.")

    elif choice == 2:
        amt = int(input("Enter the amount to withdraw = "))
        if amt <= bal:
            bal -= amt
            trans.append(f"Withdraw: {amt}")
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    elif choice == 3:
        print("Current Balance =", bal)

    elif choice == 4:
        if not trans:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for t in trans:
                print(t)

    elif choice == 5:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
