from abc import ABC, abstractmethod


class Quadrilateral(ABC):

    def __init__(self, coordinates):
        self.coordinates = coordinates

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
