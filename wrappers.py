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
print("-"*40)

#Method decorator
def decorator(func):
    def wrapper(self, *args, **kwags):
        print("Before method execution")
        res = func(self, *args, **kwags)
        print("After method excecution")
        return res
    return wrapper

class Myclass:
    @decorator
    def say_hello(self):
        print("Hello!")
obj1 = Myclass()
obj1.say_hello()
print("-"*40)
#Built-in Decorators
#1. @staticmethod
class MathOperations:
    @staticmethod
    def add (x, y):
        return x+y
res = MathOperations.add(4,5)
print(res)
print("-"*40)
#2. @classmethod
class Employee:
    raise_amount = 1.05
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary

    @classmethod
    def set_raised_amount(cls, amount):
        cls.raise_amount = amount
#Using the class method
Employee.set_raised_amount(1.10)
print(Employee.raise_amount)
print("-"*40)
#3. @property 
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# Using the property
c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)
        



