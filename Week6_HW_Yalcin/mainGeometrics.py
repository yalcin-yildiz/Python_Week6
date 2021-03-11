from dersler_total.Week6_HW_Yalcin.geometrics import *

print("Welcome to the Geometrics class")

while True:
    print("Please select the option below")
    choice = int(input("1- Triangle\n2- Rectangle\n3- Square\n4- Cube\n5- Pyramid\n6- Exit\n"))

    if choice == 1:
        side1 = input("Please enter side1: ")
        side2 = input("Please enter side2: ")
        side3 = input("Please enter side3: ")

        myTriangle = Triangle(int(side1), int(side2), int(side3))

        print("The perimeter of the triangle is " + str(myTriangle.perimeter()))
        print("The area of the triangle is " + str(myTriangle.area()))

    elif choice == 2:
        side1 = input("Please enter side1: ")
        side2 = input("Please enter side2: ")

        myRectangle = Rectangle(int(side1), int(side2))

        print("The perimeter of the rectangle is " + str(myRectangle.perimeter()))
        print("The area of the rectangle is " + str(myRectangle.area()))

    elif choice == 3:  # Square
        side1 = int(input("Please enter side: "))

        mySquare = Square(side1)

        print("The perimeter of the Square is " + str(mySquare.perimeter()))
        print("The area of the Square is " + str(mySquare.area()))

    elif choice == 4:  # Cube
        side1 = int(input("Please enter side: "))

        myCube = Cube(side1)

        print("The volume of the Cube is " + str(myCube.volume()))

    elif choice == 5:  # Pyramid
        side1 = int(input("Please enter side1 of triangle: "))
        side2 = int(input("Please enter side2 of triangle: "))
        side3 = int(input("Please enter side3 of triangle: "))

        sideOfBase = int(input("Please enter the side of base Square: "))
        height = int(input("Please enter the height of Pyramid"))
        myPyramid = Pyramid(side1, side2, side3, sideOfBase, height)

        print("The volume of the Pyramid is " + str(myPyramid.volume()))

    elif choice == 6:
        break
    else:
        print("Try again")
