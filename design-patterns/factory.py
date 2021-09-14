"""
This is an example of a design pattern using factory method

Factory encapsulates object creation, i.e., Factory is an object specialized in creating other objects

Factory patterns are useful when
    * You are not sure what types of objects you will eventually need in your system
    * Your application needs to decide on what classes to use at runtime

Example - Pet store program

Original the program had only the Dog class. When a new class for Cat has to be added, the factory
method comes in handy
"""

class Dog:

    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:

    """A new cat method"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):

    """The factory method"""

    pets = dict(dog=Dog(name="Hope"), cat=Cat(name="Peace"))

    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())