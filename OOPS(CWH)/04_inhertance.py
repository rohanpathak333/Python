class Animal: #Parent class(super class)
    location = "australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic Animal Sound")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self): # we override the speak method
      
        print("Woof!")
        super().speak() # We are using the speak function of the parent class and print generic animal sound


# a = Animal("Dogo")
# a.speak()

d = Dog("bruno")
d.speak()
print(d.location)

a = Animal("Dogo")
a.speak()
