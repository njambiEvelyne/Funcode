import functools
import operator
from functools import reduce
import emoji

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
print(emoji.emojize(":red_heart: ")*20)

#filter 
def start_a(w):
  return w.startswith("a")

li=["apples", "banana", "avocado", "cherry", "apricot"]
res6 = filter(start_a, li)
print(list(res6))

def even(n):
  return n % 2 ==0
a=[1,2,3,4,5,6]
b = filter(even, a)
print(list(b))

def odd(r):
  return r % 2 !=0
d = [1,4,6,8,9,2,23]
f = filter(odd, d)
print(list(f))
print("-"*40)

#filter with lambda
a = [1,2,3,4,6,8,9]
b = filter(lambda s: s %2 ==0, a)
print(list(b))
c = map(lambda c: "Even" if c % 2 == 0 else "Odd", a)
print(list(c))


