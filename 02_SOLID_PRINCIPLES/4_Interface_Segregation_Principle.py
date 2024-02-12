''' 
The Principle of interface segregation states that a client should not be forced
to implement an interface that it doesn't use. if an interface has methods that a 
client doesn't need, then it is considered "fat" or "unsegregated" and violates the 
principle of interface segregation. 

''' 

# Here is an example of a system that violates the interface segregation principle.

class Superhero:
    def fly(self):
        pass
    def super_strength(self):
        pass
    def invisibility(self):
        pass

class Superman(Superhero):
    def fly(self):
        #code to fly
        pass
    def super_strength(self):
        # code to use super_Strength
        pass
    def invisibility(self):
        #code to use invisibility
        pass

class Spiderman(Superhero):
    def fly(self):
        #code to fly
        pass
    def super_strength(self):
        # code to use super_Strength
        pass
    def invisibility(self):
        #code to use invisibility
        pass

class Batsman(Superhero):
    def fly(self):
        #code to fly
        pass
    def super_strength(self):
        # code to use super_Strength
        pass
    def invisibility(self):
        #code to use invisibility
        pass

class Ironman(Superhero):
    def fly(self):
        #code to fly
        pass
    def super_strength(self):
        # code to use super_Strength
        pass
    def invisibility(self):
        #code to use invisibility
        pass


''' 
In the above example, Base class defines three methods and the derived class such 
as Spiderman doesn't fly and not have invisibility power.This means spiderman 
class is forced to implement the fly and invisibility methods of the superhero class
even though it does not use them.This violates the principle of interface segregation,
as it forces clients to depend on methods they do not use.
'''

# Here is an example of a system that does not violates the interface segregation principle.

class Flyer:
    def fly(self):
        pass

class SuperStrength:
    def super_strength(self):
        pass 

class Invisible:
    def invisibility(self):
        pass

class Superman(Flyer,SuperStrength):
    def fly(self):
        #code to fly
        pass
    def super_strength(self):
        # code to use super_Strength
        pass

class Spiderman(SuperStrength):
    def super_strength(self):
        # code to use super_Strength
        pass

class Batsman(SuperStrength):
    def super_strength(self):
        # code to use super_Strength
        pass

class Ironman(Flyer,SuperStrength):
    def fly(self):
        #code to fly
        pass
    def super_strength(self):
        # code to use super_Strength
        pass


''' 
In this revised version, Superman,Spiderman,Batsman and Ironman classes only implement
the methods that are relevant to their abilites. This follows the principle of 
interface segregation, as it ensures that clients are not forced to depend on interfaces
they do not use.

'''