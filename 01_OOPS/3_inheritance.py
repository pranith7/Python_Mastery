""" 
Inheritance

Inheritance is a fundamental concept in object-oriented programming languages. It allows a class to inherit properties and behaviors from another
class, known as the superclass or base class. The class that inherits from the superclass is called the subclass or derived class.

One of the main benefits of inheritance is that it allows for code reuse. For example, let's say you have a superclass called Animal that has a
method called move(). This method could be used to describe the general movement of all animals. Then, you have a subclass called Dog that
inherits from Animal. The Dog class can reuse the move() method from the Animal class, and it can also have additional methods and properties
that are specific to dogs.

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("moving...")


class Dog(Animal):
    def bark(self):
        print("woof !")


dog1 = Dog("buddy")
dog1.bark()
dog1.move()
