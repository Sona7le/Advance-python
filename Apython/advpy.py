students = {}
courses = {}
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    students[sid] = {
        "name": name,
        "courses": {},
        "attendance": {}
    }
    print("Student added successfully!\n")
def add_course():
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")
    courses[cid] = cname
    print("Course added successfully!\n")
def assign_course():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")

    if sid in students and cid in courses:
        students[sid]["courses"][cid] = 0
        students[sid]["attendance"][cid] = 0
        print("Course assigned successfully!\n")
    else:
        print("Student or Course not found!\n")
def add_marks():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")
    marks = int(input("Enter Marks: "))

    if sid in students and cid in students[sid]["courses"]:
        students[sid]["courses"][cid] = marks
        print("Marks added successfully!\n")
    else:
        print("Invalid Student or Course!\n")
def add_attendance():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")
    attendance = int(input("Enter Attendance (%): "))

    if sid in students and cid in students[sid]["attendance"]:
        students[sid]["attendance"][cid] = attendance
        print("Attendance updated successfully!\n")
    else:
        print("Invalid Student or Course!\n")
def student_report():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("\nStudent Name:", students[sid]["name"])
        for cid in students[sid]["courses"]:
            print(
                "Course:", courses[cid],
                "| Marks:", students[sid]["courses"][cid],
                "| Attendance:", students[sid]["attendance"][cid], "%"
            )
        print()
    else:
        print("Student not found!\n")
def course_report():
    cid = input("Enter Course ID: ")

    if cid in courses:
        print("\nCourse Name:", courses[cid])
        for sid in students:
            if cid in students[sid]["courses"]:
                print(
                    "Student:", students[sid]["name"],
                    "| Marks:", students[sid]["courses"][cid],
                    "| Attendance:", students[sid]["attendance"][cid], "%"
                )
        print()
    else:
        print("Course not found!\n")
while True:
    print("1. Add Student")
    print("2. Add Course")
    print("3. Assign Course")
    print("4. Add Marks")
    print("5. Add Attendance")
    print("6. Student Report")
    print("7. Course-wise Report")
    print("8. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        assign_course()
    elif choice == "4":
        add_marks()
    elif choice == "5":
        add_attendance()
    elif choice == "6":
        student_report()
    elif choice == "7":
        course_report()
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")
