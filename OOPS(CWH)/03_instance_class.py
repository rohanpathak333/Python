class Employee:
    company = "Asus" #This is class attribute

    def __init__(self, salary, name, bond,company):
        self.salary= salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

        def get_salary(self):
            return self.salary
        def get_info(self):
            print(f"The name of the employee is {self.name}. Salary is {self.salary}. THe bond is for {self.bond} years")

e1 = Employee(3400,"John",3 ,"HCL")
print(e1.company)# will always print instance attribute whenever present
print(Employee.company)# this will always print the class attribute