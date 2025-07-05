# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The sum is {a+b}")

#     except:
#         print("Some error occurred!")

# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The sum is {a+b}")

#     except ValueError:
#         print("Please dont perform bad typecasts")

#     except ZeroDivisionError:
#         print("Hey dont divide by 0")

#     except Exception as e:
#         print("Some error occurred! bhai", e)



#raising exceptions
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please dont divide by 0")

print(f"The division is {a / b}")
