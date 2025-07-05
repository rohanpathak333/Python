#Decorator is a function that takes a function, it creates a new function inside its body(wrapper).
#Then it retyrns that new function
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function......")
    return wrapper

#1 method to use decorator    
@decorator    
def say_hello():
    print("Hello!")

say_hello()

# 2nd method to use decorator
# f = decorator(say_hello)
# f()

