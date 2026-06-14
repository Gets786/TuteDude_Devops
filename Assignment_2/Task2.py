student = {
    "GK": "A"
}

while True:

    print("\nChoose any option")
    print("1. Insert an element in dictionary")
    print("2. Update an existing element in dictionary")
    print("3. Exit")

    ch = int(input("Enter your choice (1, 2 or 3): "))

    if ch == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")

        student[name] = grade

        print("\nCurrent Dictionary:")
        for name, grade in student.items():
            print(name, ":", grade)

    elif ch == 2:
        name = input("Enter student name to update: ")

        if name in student:
            grade = input("Enter new grade: ")
            student[name] = grade
            print("Record updated successfully!")
        else:
            print("Student not found!")

        print("\nCurrent Dictionary:")
        for name, grade in student.items():
            print(name, ":", grade)

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")