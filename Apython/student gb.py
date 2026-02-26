# Student Gradebook with Grade

gradebook = {}

def get_grade(marks):
    if marks >= 90:
        return "O"
    elif marks >= 80:
        return "E"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    grade = get_grade(marks)
    gradebook[name] = (marks, grade)
    print("Student added with grade:", grade)

def view_students():
    if not gradebook:
        print("No records found.")
    else:
        print("\nStudent Records:")
        for name, data in gradebook.items():
            marks, grade = data
            print(name, "- Marks:", marks, "| Grade:", grade)

def calculate_average():
    if not gradebook:
        print("No data to calculate average.")
    else:
        total = sum(marks for marks, grade in gradebook.values())
        avg = total / len(gradebook)
        print("Class average:", avg)

while True:
    print("\n--- Student Gradebook Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
