"""
Encapsulation is the practice of bundling data and related actions together into a single unit, 
usually referred to as a class. This helps keep the implementation details hidden away from other
parts of your program, improving modularity, security, and maintenance. To achieve encapsulation, 
access control mechanisms—like public, private, protected attributes—are employed to limit direct 
interaction with the underlying variables. Although true privacy does not exist in Python due to 
lack of access specifiers, conventions around naming can help indicate intended usage.

Consider the following example illustrating encapsulation principles in Python:

"""


class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self._model = model  # Protected attribute
        self.__speed = 0  # Private attribute

    # Public method to access private attribute
    def get_speed(self):
        return self.__speed

    # Public method to modify protected attribute
    def set_model(self, new_model):
        self._model = new_model

    def accelerate(self, increment):
        self.__speed += increment

    def brake(self, decrement):
        self.__speed -= decrement
        if self.__speed < 0:
            self.__speed = 0


# Instantiate the class
my_car = Car(make="Toyota", model="Camry")

# Accessing public, protected, and private attributes
print("Make:", my_car.make)  # Public attribute
print("Model:", my_car._model)  # Protected attribute (convention)
print(
    "Speed:", my_car.get_speed()
)  # Accessing private attribute through a public method

# Modifying protected attribute using a public method
my_car.set_model("Corolla")
print("Updated Model:", my_car._model)

# Accelerate the car
my_car.accelerate(20)
print("Speed after acceleration:", my_car.get_speed())

# Brake the car
my_car.brake(10)
print("Speed after braking:", my_car.get_speed())

""" 
In this example:

make is a public attribute.
_model is a conventionally protected attribute.
__speed is a private attribute.

It's important to note that Python relies on the developer's discipline to follow these conventions, 
as there are no strict rules enforcing access modifiers. The use of public methods to interact with 
private or protected attributes helps maintain encapsulation.
"""
