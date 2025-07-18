student_data = []
def update_student_data():
    sid = input("Enter Student's ID: ")
    found = False

    for student in student_data:
        if student["id"] == sid:
            print(f"\n Student found: {student['name']}")

            name = input("Enter new name (press Enter to keep current): ")
            age_input = input("Enter new age (press Enter to keep current): ")
            grade = input("Enter new grade (press Enter to keep current): ")
            dob = input(
                "Enter new DOB (YYYY-MM-DD) (press Enter to keep current): ")
            subjects_input = input(
                "Enter new subjects (comma-separated) (press Enter to keep current): ")

            if name:
                student["name"] = name
            if age_input:
                student["age"] = int(age_input)
            if grade:
                student["grade"] = grade
            if dob:
                student["dob"] = dob
            if subjects_input:
                student["subjects"] = [sub.strip()
                                       for sub in subjects_input.split(",")]

            print("Student updated successfully!")
            found = True
            break

    if not found:
        print("Student not found.")
while True:

    print("Welcome to the student Data Organizer!")
    print("Select an Option:")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student Information")
    print("4. Delete Student")
    print("5. Display subjects offered")
    print("6. Exit")

    choice = input("Enter your choice:")
    print("")
    print("")

    if choice == "1":
        print("Enter student details:")
        student_id = input("Enter student id: ")
        student_name = input("Enter student name: ")
        student_age = input("Enter student age: ")
        student_grade = input("Enter student grade:")
        student_birthdate = input("Enter studnet birthdate (YYYY-MM-DD):")
        student_subjects = input("ENter student subjects(comma-separated):")
        print(f"Student {student_name} added successfully!")
        student_data.append({"id": student_id, "name": student_name, "age": student_age, "grade": student_grade, "birthdate": student_birthdate, "subjects": student_subjects})

        print("")   
        print("")

        print("Select an option:")
        print("1. Add Student")
        print("2. Display all students")
        print("...")
        print("")
        print("")

        print("--- Display All students ---")
        print("")
        print("")


    elif choice == "2":
        print(student_data )
    elif choice == "3":
        update_student_data()
    elif choice == "4":
        sid = input("Enter Student's ID to delete: ")
        found = False

        for student in student_data:
            if student["id"] == sid:
                student_data.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("No student found with that ID.")
    elif choice == "5":
        print("Subjects Offered:")
        subjects = set()
        for student in student_data:
            subjects.update(student["subjects"])
        for subject in subjects:
            print(f" - {subject}")
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
        update_student_data()
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        print("")
        print("")
