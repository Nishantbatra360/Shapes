from Rectangle import Rectangle


class Square(Rectangle):
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
        if upper_width == bottom_width and left_height == right_height and right_height == upper_width and is_right_angle:
            self.side = upper_width
            super().__init__(coordinates)
        else:
            raise NotImplementedError("Coordinates not valid for square")

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def draw(self):
        shape = ""
        for i in range(self.side):
            shape = shape + "*"
            for j in range(self.side - 2):
                if i == 0 or i == self.side - 1:
                    shape = shape + "*"
                else:
                    shape = shape + " "
            shape = shape + "*\n"
        return shape
