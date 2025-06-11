class Employee:

    def __init__(self, salary, name, bond):
        self.sal = salary #create an instance attribute of name sal and assign it with salary
        self.na = name
        self.bo = bond
    
    def get_salary(self):
        return self.sal
    
    def get_info(self):
        print(f"The name of the employee is {self.na}. Salary is {self.sal}. The bond is for {self.bo} years ")


e1 = Employee(3400,"John Doe", 4)
print(e1.get_salary())

    