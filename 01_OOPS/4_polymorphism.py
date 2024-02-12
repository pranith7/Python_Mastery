""" 
Polymorphism

Polymorphism is a core concept in object-oriented programming languages that allows for the reuse of code through the use of inheritance and
interfaces. It refers to the ability of a single object or function to take on multiple forms depending on the context in which it is used.

There are two main types of polymorphism in object-oriented programming languages:
   Static polymorphism: Also known as compile-time polymorphism, this type of polymorphism is achieved through method overloading.
   Method overloading occurs when a class has multiple methods with the same name but different signatures (i.e., the number or type of
  arguments). When calling the method, the appropriate version is chosen based on the arguments passed.

 Dynamic polymorphism: Also known as runtime polymorphism, this type of polymorphism is achieved through method overriding. Method
 overriding occurs when a subclass defines a method with the same name and signature as a method in the superclass. When calling the
method on an instance of the subclass, the subclass's version of the method is called instead of the one in the superclass. This allows the
subclass to provide its own implementation of the method and modify or extend the behavior inherited from the superclass.

"""

""" 
 Static polymorphism
 In Python, static (or compile-time) polymorphism is typically achieved using abstract 
 base classes or interfaces in combination with inheritance. Here's an example that demonstrates this concept:
"""


class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


# Instantiate the class
math_operations = MathOperations()

# Call the overloaded add method based on the number of arguments
result_2_args = math_operations.add(2, 3)
result_3_args = math_operations.add(2, 3, 4)

print("Result with 2 arguments:", result_2_args)
print("Result with 3 arguments:", result_3_args)


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        import math

        return math.pi * (self._radius**2)


def print_shape_info(shapes):
    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.area()} units^2")


rectangles = [Rectangle(5, 10), Rectangle(3, 4)]
circles = [Circle(2), Circle(7)]

print_shape_info(rectangles)
print_shape_info(circles)

""" 
Dynamic Polymorphism

Dynamic (or runtime) polymorphism refers to the ability of objects belonging to different classes
to respond differently when they receive the same message at runtime based on their types. This is 
often implemented using method overriding in object-oriented programming languages such as Python. 

Let's consider an example involving animals:
"""
from abc import ABC, abstractmethod


# Abstract Animal Class defining sound behavior
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# Concrete Implementation Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


# Concrete Implementation Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Create instances of Dog and Cat
my_dog = Dog()
my_cat = Cat()

# Call the make_sound method on each instance
animal_sounds = [my_dog.make_sound(), my_cat.make_sound()]

for sound in animal_sounds:
    print(sound)
