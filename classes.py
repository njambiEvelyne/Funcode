import functools
import operator
from functools import reduce
class Car:
  def __init__(self, name, brand):
    self.name = name
    self.brand = brand
  def display(self):
    return self.brand, self.name
car1 = Car("Toyota", "Corolla")
print(car1.display())

class Circle:
  def __init__(self, r):
    self.r = r
  def area(self):
    a = 3.14 * self.r**2
    return f"The area of the circle is {a}"
ins = Circle(5)
print(ins.area())

a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

fruits = ["apple", "bananas", "cherry"]
res = map(str.title,fruits)
print(list(res))



def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)
res3 = reduce(lambda x, y: x+ y,a)
print(res3)
print(res)
res2 = reduce(lambda x,y: x*y, a)
print(res2)
  
#The use of reduce with operator
nums = [1,3,5,7,9]
print(functools.reduce(operator.add, nums))
print(functools.reduce(operator.mul,nums))
print(functools.reduce(operator.sub, nums))