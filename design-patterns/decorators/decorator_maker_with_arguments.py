"""This is an example of passing arguments to decorators"""
def decorator_maker_with_arguments(dargs1, dargs2, dargs3):
    def decorator(function_to_be_decorated):
        def wrapper(fargs1, fargs2, fargs3):
            """This is the wrapper function"""
            print("The wrapper can access all the variables \n"
                  "\t from the decorator maker - {0}, {1}, {2} \n"
                  "\t from the decorated function - {3}, {4}, {5} \n"
                  "and pass them to the decorated function".format(dargs1, dargs2, dargs3, fargs1, fargs2, fargs3))
            return function_to_be_decorated(fargs1, fargs2, fargs3)
        return wrapper
    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy", "Dask")
def decorated_function_with_arguments(fa1, fa2, fa3):
    print("This is the decorated function and it knows only about its arguments - {}, {}, {}".format(fa1, fa2, fa3))

decorated_function_with_arguments(pandas, "Python", "Spark")