students = []


# Add Student
def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks1 = float(input("Enter marks in Subject 1: "))
    marks2 = float(input("Enter marks in Subject 2: "))
    marks3 = float(input("Enter marks in Subject 3: "))

    student = {
        "roll": roll,
        "name": name,
        "marks1": marks1,
        "marks2": marks2,
        "marks3": marks3
    }

    students.append(student)
    print("Student added successfully!")


# Display Students
def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")

        for student in students:
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Subject 1:", student["marks1"])
            print("Subject 2:", student["marks2"])
            print("Subject 3:", student["marks3"])
            print("------------------------")


# Search Student
def search_student():
    roll = int(input("Enter Roll Number to search: "))

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Subject 1:", student["marks1"])
            print("Subject 2:", student["marks2"])
            print("Subject 3:", student["marks3"])
            return

    print("Student not found.")


# Update Student
def update_student():
    roll = int(input("Enter Roll Number to update: "))

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["marks1"] = float(input("Enter new marks in Subject 1: "))
            student["marks2"] = float(input("Enter new marks in Subject 2: "))
            student["marks3"] = float(input("Enter new marks in Subject 3: "))

            print("Student record updated successfully!")
            return

    print("Student not found.")


# Delete Student
def delete_student():
    roll = int(input("Enter Roll Number to delete: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student not found.")


# Calculate Average Marks
def calculate_average():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            average = (
                student["marks1"]
                + student["marks2"]
                + student["marks3"]
            ) / 3

            print("Name:", student["name"])
            print("Average Marks:", round(average, 2))
            return

    print("Student not found.")


# Save Records
def save_records():
    file = open("students.txt", "w")

    for student in students:
        file.write(
            str(student["roll"]) + "," +
            student["name"] + "," +
            str(student["marks1"]) + "," +
            str(student["marks2"]) + "," +
            str(student["marks3"]) + "\n"
        )

    file.close()
    print("Records saved successfully!")


# Main Program
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Save Records")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        calculate_average()

    elif choice == 7:
        save_records()

    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
  
