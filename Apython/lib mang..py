# Simple Library Management System

library = {}

def add_book():
    name = input("Enter book name: ")
    if name in library:
        print("Book already exists.")
    else:
        library[name] = "Available"
        print("Book added successfully.")

def show_books():
    if not library:
        print("No books in library.")
    else:
        print("\nBooks in Library:")
        for book, status in library.items():
            print(book, "-", status)

def issue_book():
    name = input("Enter book name to issue: ")
    if name in library and library[name] == "Available":
        library[name] = "Issued"
        print("Book issued.")
    else:
        print("Book not available.")

def return_book():
    name = input("Enter book name to return: ")
    if name in library and library[name] == "Issued":
        library[name] = "Available"
        print("Book returned.")
    else:
        print("Invalid book name.")

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
