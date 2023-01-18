class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
         return (self.length + self.width)*2


    def display(self):
      print("The area of rectangle is", self.Area())
      print("The perimeter of rectangle is", self.Perimeter())

class Rectangle(Shape):
  pass


rectangle = Shape(12,6)
rectangle2 = Rectangle(12,6)


rectangle.display()
rectangle2.display()