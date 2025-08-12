
class Shape:
    def __init__(self, name,side):
        self.name = name
        self.side = side

    def describe (self):
        print(f"This is a {self.name}")

#shape1=Shape(name="Circle")
#shape1.describe() 


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle", 4)
        self.length = length
        self.width = width

    def area(self):
        a=self.width*self.length
        print(f"For {self.name} area is {a}")
        return self.length * self.width


r1=Rectangle(3,4)
r1.describe()
r1.area()

