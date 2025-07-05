class Employee:
     def __init__(self, name , salary):
          self.name = name
          self.salary = salary

     @property     
     def first_name(self):
          l = self.name.split(" ")
          print(l)
          print(l[0])
          print(l[1])
          return l[0]
     
     @first_name.setter
     def first_name(self, first):
          l = self.name.split(" ")
          new_name = f"{first} {l[1]}"
          print("I have changed the name")
          self.name = new_name
     
e = Employee("Jack Doe", 345555)
# print(e.first_name())

# e.set_first_name("John")
# print(e.name)
     
print(e.first_name)
e.first_name = "Johny"
print(e.name)     