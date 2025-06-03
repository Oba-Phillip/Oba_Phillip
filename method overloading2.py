# method_overloading/employee_example.py
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def calculate_pay(self, *args):
        if len(args) == 1 and isinstance(args[0], (int, float)):
            # Monthly salary employee
            return args[0]
        elif len(args) == 2 and all(isinstance(x, (int, float)) for x in args):
            # Hourly employee (hours worked, hourly rate)
            hours, rate = args
            return hours * rate
        elif len(args) == 3:
            # Commission employee (base salary, sales amount, commission rate)
            base, sales, rate = args
            return base + (sales * rate)
        else:
            raise ValueError("Invalid pay calculation parameters")

# Usage
emp1 = Employee("John Doe", "E1001")
print(emp1.calculate_pay(5000))               # Monthly salary: 5000
print(emp1.calculate_pay(40, 25))             # Hourly: 1000 (40*25)
print(emp1.calculate_pay(2000, 10000, 0.1))   # Commission: 3000 (2000 + 10000*0.1)