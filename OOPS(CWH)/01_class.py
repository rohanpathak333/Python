#Class : Class is a blueprint or a template. Eg Form for an exam that contain name,age,electives,fathers's name etc

#Object: specicfic instance created from the template(class). Eg. Form which contains the data for John doe

class Employee:
    company = "HP"

    def get_salary(self): #Self is important here because self is a way to reference the object of the class which is beingh created
        return 34000
    

e = Employee() # an boject of class employee is created here
print(e.get_salary()) # Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)