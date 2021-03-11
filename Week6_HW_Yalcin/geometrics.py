"""+Create a class named Triangle and Rectangle.

+Create a subclass named Square inherited from Rectangle.

+Create a subclass named Cube inherited from Square.

Create a subclass named Pyramid multiple inherited both from Triangle and Square.

Two dimensional classes (Triangle, Rectangle and Square) should have:

its dimensions as attributes.(can be inherited from a superclass)
methods which calculate its area and perimeter separately.

Three dimensional classes (Cube and Pyramid) should have:
its dimensions as attributes which are inherited from a superclass
its extra dimensions if there is. (hint: maybe for Pyramid)
methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)"""
from math import sqrt


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    # the formula for area of triangle
    # √(s(s-a)(s-b)(s-c))
    def area(self):
        x = self.perimeter() / 2
        s1 = self.side1
        s2 = self.side2
        s3 = self.side3

        return sqrt(x * (x - s1) * (x - s2) * (x - s3))


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
        self.side = side

    def volume(self):
        return self.side ** 3


class Pyramid(Triangle, Square):
    def __init__(self, side1of_triangle, side2of_triangle, side3of_triangle, side_of_base_square, height_of_pyramid):
        Triangle.__init__(self, side1of_triangle, side2of_triangle, side3of_triangle)
        Square.__init__(self, side_of_base_square)
        self.side_of_base_square = side_of_base_square
        self.height_of_pyramid = height_of_pyramid

    def volume(self):
        return Square.area(self) * self.height_of_pyramid / 3
