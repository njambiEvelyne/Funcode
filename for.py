fruits = ["banana", "mango", "apples"]
for fruit in fruits:
  print(fruit)

#Using for together with enumerate
for index, fruit in enumerate(fruits):
  print(f"Index {index}: {fruit}")
print(" ")

for k , v in enumerate(fruits):
  print(f"Index {k}: {v}")

#Use of for in dictionaries
person = {
  "name":"Evelyne",
  "age": "19",
  "nationality":"Kenyan"
}
for key in person:
  print(key)

for value in person.values():
  print(value)
for key, value in person.items():
  print(f"{key}: {value}")
print("Basic range")
for num in range(5)  :
  print(num)
print("With start and end")
for num2 in range(0,5):
  print(num2)
print("With a step")
for num3 in range(0, 10, 2):
  print(num3)
print("Reverse")
for num4 in range(5,0, -1):
  print(num4)
print("Break statements")
numbers = [1,2,3,4,5,6,7,8,9]
for num5 in numbers:
  if num5 > 5:
    break
  print(num5)
print("Continue Statement")
for digits in range(10):
  if digits % 2==0:
    continue
  print(digits)
print("Netsed loops")
for numr in range(1,5):
  for j in range(1,5):
    print(f"{numr} * {j} = {numr*j}")
  print("___")
# string creation
str = "GFG Learning-Portal"

for i in str:
    print(i, end="")

print()
for i in range(0, len(str), 2):
    print(str[i], end="_")
#List comprehensions(This is eliminating the use of loops and instead use the lists)
b = [i **2 for i in range(1,10)]
print("Using list comprehension: ", b)


x = 0

while (x < 100):

    x+=2

print(x)



