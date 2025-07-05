#dunder methods
class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return f"The name is  {self.name} and the salary is {self.salary}"


    def __repr__(self):
        return f"name: {self.name} \nsalary: {self.salary}"

    def __len__(self):
        return len(self.name)


e = Employee("Harry", 435666)
print(e.name, e.salary)
print(str(e)) # for users to see
print(repr(e)) #mostly for developers for debugging
print(len(e))
