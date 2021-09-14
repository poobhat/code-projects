from functools import wraps

def make_blink(function):
    """Defines the decorator"""

    #functools wraps make the decorator transparent in terms of its name and docstring
    @wraps(function)

    #define the inner function ot the wrapper
    def decorator():
        #Grab the return value of the function being decorated
        ret = function()

        #Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"
    return decorator

#Apply the decorators here
@make_blink
def hello_world():
    """Original Function!"""
    return "Hello World"

#Check the results of decorating
print(hello_world())

#Check the function name is still the same as the function being decorated
print(hello_world.__name__)

#Check if te docstring is still the same as the function being decorated
print(hello_world.__doc__)