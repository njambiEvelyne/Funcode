import functools
from functools import reduce
import operator
numbers = [12,7,25,8,15,30,7,12]
#This function will find all the evens in the list of the numbers
print("Even Numbers:")
evens = filter(lambda x: x %2 ==0, numbers)
print(list(evens))

#Function to find all the numbers divisible by 5
print("Numbers Divisible by 5:")
divisible = filter(lambda r: r%5 ==0, numbers)
print(list(divisible))

#A function to find and display the squares of the numbers
square = map(lambda s: s **2, numbers)
print(list(square))

#Finding a number greater than the average
average = functools.reduce(operator.add, numbers)/len(numbers)
print(f"The average is: {average}")
# for num in numbers:
#   if num > average:
#     print(f"The following nnumbers are greater than the average:")
    
greater = filter(lambda g: g>average, numbers)
print("Numbers greater than the average:")
print(list(greater))



