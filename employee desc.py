class Employee:
    def _init_(self, id, name, basic_salary):
        self.id = id
        self.name = name
        self.basic_salary = basic_salary
    
    def _repr_(self):
        return f"Employee(id={self.id}, name='{self.name}', basic_salary={self.basic_salary})"
    
employees = [
    Employee(1, "John", 50000),
    Employee(2, "Jane", 70000),
    Employee(3, "Bob", 60000),
]

sorted_employees = sorted(employees, key=lambda emp: emp.id)

for emp in sorted_employees:
    print(emp)
