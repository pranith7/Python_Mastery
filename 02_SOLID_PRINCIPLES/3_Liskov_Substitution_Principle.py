''' 
Liskov Substitution Principle (LSP) is a principle of OOP that states that 
if a program is using a class, it should be able to use any derived class
of that class without knowing it, as long as the dervied class follows the
behaviour of the base class.

'''

# Example of class that does not follow LSP 

class Animal:
    def __init__(self,name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

class Fish(Animal):
    def __init__(self, name, fins):
        super().__init__(name)
        self.fins = fins 

''' 
In this example, the base class defines the core functionality and bird and fish
class add additional functionality through inheritance.However, it violates LSP.
because both the derived classes does not behave in the same way as base cls.

Base class does not have wingspan or fins attribute, so it is not possible to use 
a bird or fish object interchangeably with the animal object without knowing which 
specific type of object it is.

'''
# Example of class that follows LSP

class Animal:
    def __init__(self,name,wingspan=None,fins = None):
        self.name = name
        self.wingspan = wingspan
        self.fins = fins

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name,wingspan=wingspan)

class Fish(Animal):
    def __init__(self, name, fins):
        super().__init__(name,fins=fins)

''' 
In this revised design,Animal class defines the core functionality (such as storing the 
animal's name,wingspan, and fins) and the dervied classes add additional functionality
through inheritance.This follows LSP,because we can use any of the derived classes
interchangeably with the base Animal class, as long as they follow the behaviour of 
the base class.

'''