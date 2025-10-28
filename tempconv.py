import emoji # type: ignore
def to_celsius():
  fahrenheit = int(input("Enter the temperature in fahrenheit: "))
  converted_temp = (fahrenheit -32)*(5/9)
  print(emoji.emojize(f"The temperature is {converted_temp} degree celsius:sparkles:"))
  print("*"*30)
  print(emoji.emojize("Temperature converted succesfully:check_mark_button:"))
  return converted_temp



def to_fahrenheit():
  celsius = int(input("Enter the temperature in celsius: "))
  converted_temp = (celsius * 9/5) + 32
  print(emoji.emojize(f"The temperature is {converted_temp} Fahrenheit:sparkles:"))
  print("*"*30)
  print(emoji.emojize("Temperature converted succesfully:check_mark_button:"))
  return converted_temp

print("_"*40)
print("Choose for conversion from celsius to fahreheit and vice versa\n 1 for Celsius \n 2 for Fahrenheit:")
choice = int(input("Enter the conversion unit(1 or 2)"))
print("-"*40)
if choice == 1:
  to_celsius()
else:
  to_fahrenheit()

