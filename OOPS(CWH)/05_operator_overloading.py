class Point:
    def __init__(self, x, y):
        self.x = x
        self.y =y

    def sum(self, p):
        # print(self.x)
        # print(self.y)
        # print(p.x)
        # print(p.y)
        return Point((self.x + p.x), (self.y +p.y))

    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3,2)
p2 = Point(6, 4)
p = p1.sum(p2)  #returns a new point which is a sum of p1 and p2

# p =p1 + p2 # we overloaded the + operator by writing __add__ function
p.print_point()