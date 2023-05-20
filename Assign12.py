"""
Company maintains employee
information as employee ID,
name, designation and salary.
Allow user to add, delete
information of employee. Display
information of particular
employee. If employee does not
exist an appropriate message is
displayed. If it is, then the system
displays the employee details. Use
index sequential file to maintain
the data.
"""



INDEX_FILE = "employee_index.txt"
DATA_FILE = "employee_data.txt"
EMPLOYEE_RECORD_WIDTH = 125

class Employee:
    def __init__(self, emp_id, name, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary
    
    def to_record(self):
        record = f"{self.emp_id:05d}{self.name:<50}{self.designation:<50}{self.salary:10.2f}"
        return record

    @classmethod
    def from_record(cls, record):
        emp_id = int(record[:5])
        name = record[5:55].strip()
        designation = record[55:105].strip()
        salary = float(record[105:])
        return cls(emp_id, name, designation, salary)

def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    with open(INDEX_FILE, "r") as index_file:
        existing_ids = [line[:5] for line in index_file.readlines()]
        if str(emp_id).zfill(5) in existing_ids:
            print("Employee with ID", emp_id, "already exists.")
            return

    name = input("Enter Employee Name: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(emp_id, name, designation, salary)
    with open(INDEX_FILE, "a") as index_file, open(DATA_FILE, "a") as data_file:
        index_file.write(str(emp_id).zfill(5) + "\n")
        data_file.write(employee.to_record() + "\n")

    print("Employee added successfully.")

def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    with open(INDEX_FILE, "r") as index_file:
        lines = index_file.readlines()
        for i, line in enumerate(lines):
            if line[:5] == str(emp_id).zfill(5):
                lines[i] = "-" * 5 + "\n"
                with open(INDEX_FILE, "w") as updated_index_file:
                    updated_index_file.writelines(lines)
                print("Employee deleted successfully.")
                return

    print("Employee with ID", emp_id, "does not exist.")

def display_employee():
    emp_id = int(input("Enter Employee ID: "))

    with open(INDEX_FILE, "r") as index_file, open(DATA_FILE, "r") as data_file:
        index_lines = index_file.readlines()
        data_lines = data_file.readlines()

        for i, line in enumerate(index_lines):
            if line[:5] == str(emp_id).zfill(5):
                data_record = data_lines[i]
                employee = Employee.from_record(data_record)
                print("Employee Details:")
                print("Employee ID:", employee.emp_id)
                print("Name:", employee.name)
                print("Designation:", employee.designation)
                print("Salary:", employee.salary)
                return

    print("Employee with ID", emp_id, "does not exist.")

def main():
    choice = 0

    while choice != 4:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Display Employee Information")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()
        elif choice == 2:
            delete_employee()
        elif choice == 3:
            display_employee()
        elif choice == 4:
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()