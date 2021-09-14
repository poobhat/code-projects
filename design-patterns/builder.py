class Director():
    '''The Director class'''
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tire()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

class Builder():
    '''The abstract builder class'''

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    '''The concrete builder class'''

    def add_model(self):
        self.car.model = 'Skylark'

    def add_tire(self):
        self.car.tire = 'Regular tires'

    def add_engine(self):
        self.car.engine = 'Turbo'

class Car():
    '''The final product'''

    def __init__(self):
        self.model = None
        self.tire = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tire, self.engine)

# Instantiate concrete builder
builder = SkyLarkBuilder()
# Create a director
director = Director(builder)
director.construct_car()
# invoke car method
car = director.get_car()
print(car)