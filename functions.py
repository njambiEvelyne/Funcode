import emoji # type: ignore
def evenOdd(x):
  if (x%2==0):
    print(f"{x} is an even number")
  else:
    print("The number is odd")

print(evenOdd(46))
print(evenOdd(31))

#Use of *args and *kwags
def myFun(*args,**kwargs):
  print("Non-keywords arguments (*args): ")
  for arg in args:
    print(arg)
  
  print("\nKeyword Arguments (**kwargs):")
  for key, value in kwargs.items():
    print(f"{key} == {value}")
    
#**kwags usecase
def introduce_yourself(**kwags):
  print("Let me introduce myself! ")
  for key, value in kwags.items():
    print(f"My {key} is {value}")

#Calling the function
introduce_yourself(name = "Evelyne Njambi", age = 19, city ="Paris", hobby = "coding" )

#Case 2
def create_profile(**user_info):
  print("Creating your beautiful profile, Evelyne!")
  print(emoji.emojize(":sparkles: ")*20)
  for field, info in user_info.items():
    print(f"{field.title()}:{info}")
  print("-" * 30)
  print("Profile completed!")
  print(emoji.emojize(":check_mark_button: ")*17)

create_profile(
  username ="eva254",
  age= 19,
  favourite_color = "white",
  superpower = "coding magic",
  spirit_animal = "unicorn"
)

def place_order(**fulldaymenu):
  print("*" * 30)
  for time, meal in fulldaymenu.items():
    print(f"During {time.title()}, I would like to have {meal.title()}. Thank you!")
  print("*" * 30)
  
place_order(
  morning = "Tea, 2Eggs, 1Sausage",
  midmorning = "porridge",
  lunch = "Mukimo",
  dinner = "buffet"

)
#Combining **kwargs with regular Parameters
print("We deliver all types of commodities, be it clothes, food,textile, acessories! We've got you")
def jade(clothes, food, **extras):
  print(emoji.emojize(":red_heart:  ")*20)
  print("I CONFIRM THIS IS THE ORDER I WANT!")
  print(f"I have ordered for {clothes}, \n{food}")
  if extras:
    print(emoji.emojize(":blue_heart: ")*20)
    for type, amount in extras.items():
      print("\nADDITONAL ITEMS (Separate Order):")
      print(f"I add {amount} of {type} to the initial order!")
    print("`" *30)
    print(emoji.emojize("THANK YOU FOR SHOPPING WITH US:red_heart:"))
jade(
  clothes= "1 jacket, 2 sweat pants, 4 langaries",
  food="1pizzz,2 chicken packs",
  appliences = "Microwave, 32` TV, Laptop",
  textile = "Carpet(1 piece), duvet(6*6)",

)

print(emoji.emojize(":star:")*10)

print(emoji.emojize(":down_arrow:"))
#Using the *args
def tools(*args):
  for arg in args:
    print(arg)
tools("pliers", "Cables", "Shovel", "plaster")