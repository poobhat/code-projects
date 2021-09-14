import copy

class Prototype:
    '''
    Prototype class has four different methods
    1. init method : Initializes dictionary object that contains objects to be cloned
    2. register_object : Registers the object to be cloned
    3. unregister_object :
    4. clone

    '''

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj): # Name will be used as a key for storing the object in the dictionary
        '''Register an object'''
        self._objects[name] = obj

    def unregister_object(self, name):
        '''Unregister an object'''
        del self._objects[name]  # This will delete the object from the dictionary

    def clone(self, name, **attr):
        '''Clone a registered object and update its attributes'''
        obj = copy.deepcopy(self._objects[name])    # Copies without changing the attributes of the original
        obj.__dict__.update(attr) # Attributes of the original is updated
        return obj

class Car:
    '''Prototypical object to be cloned'''
    def __init__(self):
    # Initializing each car object using attributes
        self.name = 'Skylark'
        self.color = 'Red'
        self.options = 'EX'

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)

c = Car()
prototype = Prototype()
prototype.register_object('Skylark', c)
c1 = prototype.clone('Skylark')
print(c1)
