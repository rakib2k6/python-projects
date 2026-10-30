
students = [
    {
        "id": 101,
        "name": "Rahim",
        "department": "CSE",
        "marks": 85
    },
    {
        "id": 102,
        "name": "Karim",
        "department": "EEE",
        "marks": 78
    }
]


# ------- View Student Details -------
def view_students():
    if not students:
        print("No students found!")
    else:
        print("\n------ All Students ------")

        for student in students:
            print("Student ID:", student["id"])
            print("Student Name:", student["name"])
            print("Department:", student["department"])
            print("Marks:", student["marks"])
            print("--------------------------")


# ------- Add New Student -------
def add_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == student_id:
            print("This student already exists!")
            break
    else:
        s_name = input("Enter Student Name: ").strip().title()
        s_department = input("Enter Department: ").strip().upper()
        s_marks = int(input("Enter Student Marks: "))

        if s_marks < 0 or s_marks > 100:
            print("Marks must be between 0 and 100!")
            return

        new_student = {
            "id": student_id,
            "name": s_name,
            "department": s_department,
            "marks": s_marks
        }

        students.append(new_student)
        print("New student added successfully!")


# ------- Search Student -------
def search_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Student Name:", student["name"])
            print("Department:", student["department"])
            print("Marks:", student["marks"])
            break
    else:
        print("Student not found!")


# ------- Update Student -------
def update_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == student_id:
            print("Student Found!")

            student["name"] = input(
                "Enter New Name: "
            ).strip().title()

            student["department"] = input(
                "Enter New Department: "
            ).strip().upper()

            new_marks = int(input("Enter New Marks: "))

            if new_marks < 0 or new_marks > 100:
                print("Marks must be between 0 and 100!")
                return

            student["marks"] = new_marks

            print("Student updated successfully!")
            break
    else:
        print("Student not found!")


# ------- Delete Student -------
def delete_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            break
    else:
        print("Student not found!")


# ------- Main Menu -------
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")
