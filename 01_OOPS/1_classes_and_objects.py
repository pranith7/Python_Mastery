class MyClass:
    def __init__(self):
        self._protected_variable = 42  # Protected variable

    def public_method(self):
        print("This is a public method.")
        self._protected_method()  # Accessing protected method within the class

    def _protected_method(self):
        print("This is a protected method.")


# Instantiate the class
obj = MyClass()

# Accessing public method, which in turn accesses the protected method
obj.public_method()

# Attempting to access the protected method directly from outside the class is technically allowed,
# but it is discouraged by convention and considered as protected behavior.
# obj._protected_method()


class MyClass:
    def __init__(self):
        self.__private_variable = 42  # Private variable

    def public_method(self):
        print("This is a public method.")
        self.__private_method()  # Accessing private method within the class

    def __private_method(self):
        print("This is a private method.")


# Instantiate the class
obj = MyClass()

# Accessing public method, which in turn accesses the private method
obj.public_method()

# Attempting to access the private method directly from outside the class will result in an AttributeError
# Uncommenting the line below will raise an error
# obj.__private_method()


class SuperHero:
    def __init__(self, name, powers, team):
        self.name = name
        self.powers = powers
        self.team = team

    def FightCrime(self):
        print(f"{self.name} can fight crimes in neighbourhood.")

    def SaveWorld(self):
        print(f"{self.name} can save world from aliens")


class SuperVillain:
    def __init__(self, name, powers, evil_plan):
        self.name = name
        self.powers = powers
        self.evil_plan = evil_plan

    def CauseTrouble(self):
        print(f"{self.name} has taken attempt to take over the universe.")

    def AttemptToTakeOverWorld(self):
        print(f"To stop attempt of {self.name} every hero united to svae world")


superhero1 = SuperHero(
    "Spider Man", ["Web slinging", "Agility", "Spidy sense"], "Avengers"
)

print(superhero1.name)
print(superhero1.powers)
print(superhero1.team)

superhero1.FightCrime()
superhero1.SaveWorld()

superhero1.powers.append("Super Strength")
print(superhero1.powers)

superhero2 = SuperHero("Iron Man", ["Rich", "Intelligent"], "Solo or Avengers")

print(superhero2.name)
print(superhero2.powers)
print(superhero2.team)

superhero2.FightCrime()
superhero2.SaveWorld()

superhero2.powers.append("Future Sight")
print(superhero2.powers)


villian1 = SuperVillain(
    "Thanos the Slaughterer",
    ["Huge Army", "Super Strength", "Smart"],
    "Try to reduce half of the population by infinity stones",
)

print(f"Powers of {villian1.name} ")
for power in villian1.powers:
    print(power)

print(villian1.evil_plan)

villian1.AttemptToTakeOverWorld()
villian1.CauseTrouble()
