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

    
  