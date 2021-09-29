from Parallelogram import Parallelogram
from Rectangle import Rectangle
from Square import Square
from Trapezoid import Trapezoid


def display_shapes_options():
    print("1. Rectangle")
    print("2. Square")
    print("3. Trapezoid")
    print("4. Parallelogram")
    print("5. Quit")


def display_coordinates_options():
    print("1. Use stored coordinates")
    print("2. Enter coordinates")


def input_validations(message, accepted_input, minimum_value, max_value):
    while True:
        try:
            option = input(message)
            option = int(option)
            if accepted_input and option not in accepted_input:
                print("I don't think you input right value")
            elif option < minimum_value:
                print("Minimum value should be", minimum_value)
            elif option > max_value:
                print("Maximum value should be", max_value)
            else:
                return option
        except ValueError:
            print("I don't think you input right value")
            print()


def rectangle(coordinates):
    shape = Rectangle(coordinates)
    area = shape.area()
    perimeter = shape.perimeter()
    print("\nRectangle:-")
    print("Coordinates are:-",coordinates)
    print("Area is", area, "cm")
    print("Perimeter is", perimeter, "cm")
    print(shape.draw())


def square(coordinates):
    shape = Square(coordinates)
    area = shape.area()
    perimeter = shape.perimeter()
    print("\nSquare:-")
    print("Coordinates are:-",coordinates)
    print("Area is", area, "cm")
    print("Perimeter is", perimeter, "cm")
    print(shape.draw())


def trapezoid(coordinates):
    shape = Trapezoid(coordinates)
    area = shape.area()
    perimeter = shape.perimeter()
    print("\nTrapezoid:-")
    print("Coordinates are:-",coordinates)
    print("Area is", area, "cm")
    print("Perimeter is", perimeter, "cm")
    print(shape.draw())


def parallelogram(coordinates):
    shape = Parallelogram(coordinates)
    area = shape.area()
    perimeter = shape.perimeter()
    print("\nParallelogram:-")
    print("Coordinates are:-",coordinates)
    print("Area is", area, "cm")
    print("Perimeter is", perimeter, "cm")
    print(shape.draw())


while True:
    coordinates = []
    display_shapes_options()
    choice = input_validations("Enter choice: ", [], 1, 5)
    option = 0
    if choice != 5:
        display_coordinates_options()
        option = input_validations("Enter choice: ", [], 1, 2)
    if option == 2:
        for i in range(4):
            coordinate = []
            x = input_validations("Enter x" + str(i + 1) + ": ", [], 0, 100)
            y = input_validations("Enter y" + str(i + 1) + ": ", [], 0, 100)
            coordinate.append(x)
            coordinate.append(y)
            coordinates.append(coordinate)

    if choice == 1:
        if option == 1:
            coordinates = [[1, 10], [8, 10], [8, 4], [1, 4]]
        rectangle(coordinates)
    elif choice == 2:
        if option == 1:
            coordinates = [[2, 10], [8, 10], [8, 4], [2, 4]]
        square(coordinates)
    elif choice == 3:
        if option == 1:
            coordinates = [[1, 10], [16, 10], [10, 4], [4, 4]]
        trapezoid(coordinates)
    elif choice == 4:
        if option == 1:
            coordinates = [[1, 10], [8, 10], [10, 4], [3, 4]]
        parallelogram(coordinates)
    elif choice == 5:
        break
