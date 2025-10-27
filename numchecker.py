num = int(input("Enter the number: "))
if num >0:
  print("The number is positive!")
else:
  print("The number is negative")

# defining list of strings
list1 = ["geeksforgeeks", "C++",
         "Java", "Python", "C", "MachineLearning"]

# initialises a variable
i = 0

print("Printing list items\
 using while loop")
size = len(list1)
# Implement while loop to print list items
while(i < size):
    print(list1[i])
    i = i+1

i = 0

print("Printing list items\
 using do while loop")

# Implement do while loop to print list items
while(True):
    print(list1[i])
    i = i+1
    if(i < size and len(list1[i]) < 10):
        continue
    else:
        break
    
for i in range(1,5):
   for j in range (i):
      print(i, end=" ")
    #print()