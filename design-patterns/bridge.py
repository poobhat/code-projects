
class DrawAPIOne:
    '''Implementation-dependent class : Concrete class one'''

    def draw_circle(self, x, y, radius):
        print("Api one for drawing the circle at {}, {} of radius {}".format(x, y, radius))

class DrawAPITwo:
    '''Implementation-dependent class: Concrete class two'''

    def draw_circle(self, x, y, radius):
        print("Api two for drawing the circle at {}, {} of radius {}".format(x, y, radius))

class Circle(object):
    '''Implementation-independent circle abstraction'''

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api


    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent


circle1=Circle(1,2,3,DrawAPIOne())
circle1.draw()

circle2=Circle(2,3,4,DrawAPITwo())
circle2.draw()