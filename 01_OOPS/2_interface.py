from abc import ABC, abstractmethod


class Shape(metaclass=abc.ABCMeta):
    # @abc.abstractclassmethod
    @abstractmethod
    def area(self):
        pass

    # @abc.abstractmethod
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def size(self):

        pass


rec = Rectangle(45, 10)

print(rec.area())
print(rec.perimeter())
