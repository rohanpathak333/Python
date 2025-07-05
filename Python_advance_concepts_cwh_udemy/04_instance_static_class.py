class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    #instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print (info)

    #Static Method
    @staticmethod
    def sum(a, b):
        return a + b
    
    #Class method
    #whenever you need to refer class use class method
    @classmethod
    def print_company(cls):
        print(cls.company)

    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 4255)
# print(Employee.company)
# print(Employee.name) # this will throw an error
e1.print_info()
e2.print_info()

print(e2.sum(5,23))  #if static method was not created then e2 whould have been passed automatically as 1st parameter

e1.print_company()
e1.change_company("Acer")
e1.print_company()
print(Employee.company)