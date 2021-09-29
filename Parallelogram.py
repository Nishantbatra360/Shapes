from Trapezoid import Trapezoid


class Parallelogram(Trapezoid):
    def __init__(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[2]
        x4, y4 = coordinates[3]
        upper_width = x2 - x1
        left_height = y1 - y4
        right_height = y2 - y3
        bottom_width = x3 - x4
        if upper_width == bottom_width and left_height == right_height:
            self.height = abs(left_height)
            self.base = upper_width
            self.side = left_height + abs(x4 - x1)
            self.tilt_difference = x4 - x1
            self.tilt_per_row = self.tilt_difference / left_height

            super().__init__(coordinates)
        else:
            raise NotImplementedError("Coordinates not valid for parallelogram")

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * (self.base + self.side) / self.height

    def draw(self):
        shape = ""
        is_tilt_left = self.tilt_difference < 0
        is_tilt_right = self.tilt_difference > 0
        self.tilt_difference = abs(self.tilt_difference)
        if abs(self.tilt_difference) < self.side:
            self.tilt_difference = self.side
        if is_tilt_left:
            for i in range(self.height):
                for diff in range(self.tilt_difference):
                    shape = shape + " "
                self.tilt_difference = self.tilt_difference - 1
                shape = shape + "*"
                for j in range(self.base - 2):
                    if i == 0 or i == self.height - 1:
                        shape = shape + "*"
                    else:
                        shape = shape + " "
                shape = shape + "*\n"
        elif is_tilt_right:
            self.tilt_difference = 0
            for i in range(abs(self.height)):
                for diff in range(self.tilt_difference):
                    shape = shape + " "
                self.tilt_difference = self.tilt_difference + 1
                shape = shape + "*"
                for j in range(abs(self.base) - 2):
                    if i == 0 or i == abs(self.height) - 1:
                        shape = shape + "*"
                    else:
                        shape = shape + " "
                shape = shape + "*\n"
        else:
            for i in range(self.height):
                shape = shape + "*"
                for j in range(self.base - 2):
                    if i == 0 or i == self.height - 1:
                        shape = shape + "*"
                    else:
                        shape = shape + " "
                shape = shape + "*\n"
        return shape
