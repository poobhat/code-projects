class Borg:
    """ Borg class for making the class attributes global"""

    _shared_state = {}  # attribute dictionary

    def __init__(self, ):
        self.__dict__ = self._shared_state # makes it an attribute dictionary

class Singleton(Borg):
    """This class will inherit Borg class and shares all of its attributes with its various instances.
    This will essentially makes the Singleton object an object-oriented global variable"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        #Returns the attribute dictionary for printing
        return str(self._shared_state)

# Create a singleton object and add our first acronym
Singleton(HTTP = "Hypertext transfer Protocol")
cnf = Singleton()
print(cnf)

# Create another singleton object and it refers to the same attribute dictionary by adding another acronym
Singleton(SNMP = "Simple Network Management Protocol")
print(cnf)