first_names = []
last_names = []
departments = []
positions = []
wages = []
class Employee:
    def __init__(self,first_name, last_name, department, position, wage, last_names):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.department = department
        self.wage = wage
        self.last_names = last_names
    
    def sort_by_lname(self):
        ll = self.last_names.sort()
        print(ll)
        pass

    def sort_by_fname(self):
        pass

    def sort_by_department(self):
        pass

    def sort_by_wage(self):
        pass

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}\nDepartment: {self.department}\nPosition: {self.position}\nWage: {self.wage}")

def main():
    while True:
        first_name = input("Firstname: ")
        if first_name == 'q':
            return
        first_names.append(first_name)
        last_name = input("Lastname: ")
        if last_name == 'q':
            return
        last_names.append(last_name)
        department = input("Department: ")
        if department =='q':
            return
        departments.append(department)
        position = input("Position: ")
        if position == 'q':
            return
        positions.append(position)
        wage = input("Wage: ")
        if position == 'q':
            return
        wages.append(wage)

        employee = Employee(first_name,last_name,department,position,wage, last_names)
        employee.display_info()

if True:
    main()