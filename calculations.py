print("This is a calculator")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#A list of operations that can be perfomed on the values
operation = input("Enter the operation to execute: ")
#print("The operations are('+', '-', '*', '/')")
if operation =="+":
  sum = num1 + num2
  print(f"The sum is {sum}")
elif operation == "-":
  diff = num1 - num2
  print(f"The difference is {diff}")
elif operation == "*":
  product = num1 * num2
  print(f"The product is {product}")
elif operation == "/":
  if num2 == 0:
    print("Zero division error")
  else:
    div = num1 / num2
    print(f"The division result is {div}")
else:
  print("Sorry, this is not an operation!")




