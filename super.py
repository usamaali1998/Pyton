#super() = Functionn used in a child class to call methods from a parent class(superclass)
# allows <ou tto extend the functionality of inherited methods

class Shape:
    def __init__(self,color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled,  radius):
        super().__init__(color, is_filled)
        self.radius = radius



class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(self, color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        self.color = color
        self.filled = filled
        self.width = width
        self.height = height