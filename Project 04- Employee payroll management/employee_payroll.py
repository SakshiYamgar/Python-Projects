
employees = {}


# Add Employee
def add_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    allowances = float(input("Enter Allowances: "))
    deductions = float(input("Enter Deductions: "))

    if basic_salary < 0 or allowances < 0 or deductions < 0:
        print("Salary amounts cannot be negative.")
        return

    employees[emp_id] = {
        "name": name,
        "basic_salary": basic_salary,
        "allowances": allowances,
        "deductions": deductions
    }

    print("Employee added successfully!")


# Calculate Salary
def calculate_salary(emp):
    gross_salary = emp["basic_salary"] + emp["allowances"]
    net_salary = gross_salary - emp["deductions"]
    return gross_salary, net_salary


# Search Employee
def search_employee():
    emp_id = input("Enter Employee ID to search: ")

    if emp_id in employees:
        emp = employees[emp_id]
        gross, net = calculate_salary(emp)

        print("\nEmployee Found!")
        print("Employee ID:", emp_id)
        print("Name:", emp["name"])
        print("Basic Salary: Rs.", emp["basic_salary"])
        print("Gross Salary: Rs.", gross)
        print("Net Salary: Rs.", net)
    else:
        print("Employee not found.")


# Generate Payslip
def generate_payslip():
    emp_id = input("Enter Employee ID: ")

    if emp_id not in employees:
        print("Employee not found.")
        return

    emp = employees[emp_id]
    gross, net = calculate_salary(emp)

    print("\n========== EMPLOYEE PAYSLIP ==========")
    print("Employee ID :", emp_id)
    print("Employee Name:", emp["name"])
    print("--------------------------------------")
    print("Basic Salary : Rs.", emp["basic_salary"])
    print("Allowances   : Rs.", emp["allowances"])
    print("Gross Salary : Rs.", gross)
    print("Deductions   : Rs.", emp["deductions"])
    print("--------------------------------------")
    print("Net Salary   : Rs.", net)
    print("======================================")


# Save Payroll Data
def save_payroll_data():
    with open("employees.txt", "w") as file:
        for emp_id, emp in employees.items():
            gross, net = calculate_salary(emp)

            file.write(f"Employee ID: {emp_id}\n")
            file.write(f"Name: {emp['name']}\n")
            file.write(f"Basic Salary: {emp['basic_salary']}\n")
            file.write(f"Allowances: {emp['allowances']}\n")
            file.write(f"Deductions: {emp['deductions']}\n")
            file.write(f"Gross Salary: {gross}\n")
            file.write(f"Net Salary: {net}\n")
            file.write("-" * 35 + "\n")

    print("Payroll data saved successfully!")


# Main Menu
while True:
    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
    print("1. Add Employee")
    print("2. Calculate Salary")
    print("3. Generate Payslip")
    print("4. Search Employee")
    print("5. Save Payroll Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            gross, net = calculate_salary(employees[emp_id])
            print("Gross Salary: Rs.", gross)
            print("Net Salary: Rs.", net)
        else:
            print("Employee not found.")

    elif choice == "3":
        generate_payslip()

    elif choice == "4":
        search_employee()

    elif choice == "5":
        save_payroll_data()

    elif choice == "6":
        save_payroll_data()
        print("Thank you for using Employee Payroll System!")
        break

    else:
        print("Invalid choice. Please try again.")
