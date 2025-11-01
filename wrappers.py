#Wrappers are functions that enhance/modifies another function without changing its original code
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("All arguments must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))  # Works: 15
#print(calculate_area(-5, 3)) # Raises ValueError

#Function decorators
def simple_decorator(func):
    def wrapper():
        print(">>>Starting function")
        func()
        print(">>>Function finished")
    return wrapper
@simple_decorator
def greet():
    print("Hello world!")
greet()
