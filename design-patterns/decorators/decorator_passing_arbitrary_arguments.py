"""This is a general purpose decorator passing arbitrary arguments using
*args and **kwargs"""
import functools
def decorator_passing_arbitrary_arguments(function):
    @functools.wraps(function)
    def wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        '''wrapper accepting arbitrary arguments'''
        print("Positional arguments are", args)
        print("Keyword arguments are", kwargs)
        function(*args)
    return wrapper_accepting_arbitrary_arguments

def toupper(fun):
    def wrapper():
        function = fun()
        print(function.upper())
    return wrapper

@decorator_passing_arbitrary_arguments
@toupper
def function_with_no_argument():
    # print("There are no arguments")
    return "There are no arguments"

@decorator_passing_arbitrary_arguments
def function_with_positional_argument(a,b,c):
    '''Functional positional argument'''
    print(a, b, c)

@decorator_passing_arbitrary_arguments
def function_with_kwarguments():
    print("This will show keyword arguments")

# function_with_no_argument()
function_with_positional_argument(1,2,3)
# function_with_kwarguments(city="Sunnyvale", state="CA")

print(function_with_positional_argument.__name__)
print(function_with_positional_argument.__doc__)