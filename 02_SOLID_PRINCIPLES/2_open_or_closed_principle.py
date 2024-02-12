""" 
The Open-Closed Principle(OCP) is a principle of OOP that states that software
entities(such as classes,modules, and functions) should be open for extension
but closed for modification.

"""

# Here is an example of a class that does not follow OCP
# from single_responsibility_principle import User

class Shape:
    def __init__(self, type):
        self.type = type

    def area(self):
        if self.type == "circle":
            return 3.14 * self.radius * self.radius
        elif self.type == "rectangle":
            return self.width * self.height
        else:
            return 0


""" 
In this example, the Shape class has a single method,area,which calculates the 
area of a shape based on it's type. However,this design violates OCP in OOP, because
we need to modify the area method every time we want to add a new type of 
shape or change the way the area is calculated.

"""

# Refactoring above code for OCP.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius  

class Rectangle(Shape):
    def __init__(self, width,height):
        self.width = width
        self.height = height
    
    


''' 
In this revised design, the base Shape class defines the core functionality(such as having 
an area method), and the derived circle and rectangle class add additional functionality
through inheritance. This design follows the Open-cLosed principle of OOP becoz we can 
extend the functionlality of the shape class by creating new derived classes, without modifying
the existing code.

'''