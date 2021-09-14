class Baby:
    def __str__(self):
        return "Puppy"

class Dog:
    '''One of the objects returned by the abstract factory method'''

    def __str__(self):
        '''Returns Dog object'''
        return "Dog"

    def speak(self):
        '''Returns the dog speak'''
        return "Woof!"

    def get_baby(self):
        return Baby()

class DogFactory:
    '''Concrete Factory'''

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog food"

class PetStore:
    '''A class that houses our abstract factory'''

    def __init__(self, pet_factory=None):
        '''_pet_factory is our abstract factory'''
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        # pet_baby = self._pet_factory.get_baby()

        print("Our pet is a {}".format(pet))
        print("Our pet speaks in {}".format(pet.speak()))
        print("Our pet likes to eat {}".format(pet_food))
        print("Our pet's baby is called {}".format(pet.get_baby()))

#Create a concrete factory
cn_factory = DogFactory()

#Instantiate abstract factory
ab_factory = PetStore(cn_factory)

#Invoke utility method
ab_factory.show_pet()