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
  print("-" * 30)
  for field, info in user_info.items():
    print(f"{field.title()}:{info}")
  print("-" * 30)
  print("Profile completed!\n")

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

