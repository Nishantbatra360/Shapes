from Quadrilateral import Quadrilateral


class Trapezoid(Quadrilateral):
    def __init__(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[2]
        x4, y4 = coordinates[3]
        upper_width = x2 - x1
        left_height = y1 - y4
        right_height = y2 - y3
        bottom_width = x3 - x4
        is_parallel = y1 == y2 and y3 == y4
        if is_parallel:
            self.height = left_height
            self.base_1 = upper_width
            self.base_2 = bottom_width
            self.side_1 = left_height + abs(x4 - x1)
            self.side_2 = right_height + abs(x2 - x3)
            self.tilt_difference = x4 - x1
            super().__init__(coordinates)
        else:
            raise NotImplementedError("Coordinates not valid for trapezoid")

    def area(self):
        return ((self.base_1 + self.base_2) / 2) * self.height

    def perimeter(self):
        return self.side_1 + self.side_2 + self.base_1 + self.base_2

    def draw(self):
        shape = ""
        is_tilt_left = self.tilt_difference < 0
        is_tilt_right = self.tilt_difference > 0
        self.tilt_difference = abs(self.tilt_difference)
        if abs(self.tilt_difference) < self.side_1:
            self.tilt_difference = self.side_1

        is_width_increasing = self.base_2 > self.base_1
        temp_length = self.base_1

        if is_tilt_left:
            for i in range(self.height):
                for diff in range(self.tilt_difference):
                    shape = shape + " "
                self.tilt_difference = self.tilt_difference - 1
                shape = shape + "*"
                for j in range(temp_length - 2):
                    if i == 0 or i == self.height - 1:
                        shape = shape + "*"
                    else:
                        shape = shape + " "
                shape = shape + "*\n"
                if is_width_increasing:
                    if self.base_1 != self.base_2:
                        temp_length = temp_length + 2
                else:
                    if self.base_1 != self.base_2:
                        temp_length = temp_length - 2
        elif is_tilt_right:
            self.tilt_difference = 0
            for i in range(abs(self.height)):
                for diff in range(self.tilt_difference):
                    shape = shape + " "
                self.tilt_difference = self.tilt_difference + 1
                shape = shape + "*"
                for j in range(temp_length - 2):
                    if i == 0 or i == abs(self.height) - 1:
                        shape = shape + "*"
                    else:
                        shape = shape + " "
                shape = shape + "*\n"
                if is_width_increasing:
                    if self.base_1 != self.base_2:
                        temp_length = temp_length + 2
                else:
                    if self.base_1 != self.base_2:
                        temp_length = temp_length - 2
        else:
            for i in range(abs(self.height)):
                shape = shape + "*"
                for j in range(temp_length - 2):
                    if i == 0 or i == abs(self.height) - 1:
                        shape = shape + "*"
                    else:
                        shape = shape + " "
                shape = shape + "*\n"
                if is_width_increasing:
                    if self.base_1 != self.base_2:
                        temp_length = temp_length + 2
                else:
                    if self.base_1 != self.base_2:
                        temp_length = temp_length - 2
        return shape
