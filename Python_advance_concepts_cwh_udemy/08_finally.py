a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

try:
    c = a/b
    print(c)

except Exception as e:
    print(e)
# This is always executed no matter if try completely executes or not
finally:
    print("This is always executed")