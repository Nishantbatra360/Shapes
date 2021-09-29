from Parallelogram import Parallelogram


class Rectangle(Parallelogram):
    def __init__(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[2]
        x4, y4 = coordinates[3]
        upper_width = x2 - x1
        left_height = y1 - y4
        right_height = y2 - y3
        bottom_width = x3 - x4
        is_right_angle = y1 == y2 and x2 == x3 and y3 == y4 and x1 == x4
        if upper_width == bottom_width and right_height == left_height and is_right_angle:
            self.height = y1 - y3
            self.width = x2 - x1
            super().__init__(coordinates)
        else:
            raise NotImplementedError("Coordinates not valid for rectangle")

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def draw(self):
        shape = ""
        for i in range(self.height):
            shape = shape + "*"
            for j in range(self.width - 2):
                if i == 0 or i == self.height - 1:
                    shape = shape + "*"
                else:
                    shape = shape + " "
            shape = shape + "*\n"
        return shape
