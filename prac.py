import emoji # type: ignore

def store(*in_store, **need_restock):
    # Display items already in store
    if in_store:
        print(emoji.emojize(":shopping_bags: BELOW IS A LIST OF ITEMS IN STORE :down_arrow:"))
        print("━" * 40)
        for i, product_in_store in enumerate(in_store, 1):
            print(f"{i}. {product_in_store.title()}")
        print("━" * 40)
        print()  # Empty line for spacing
    
    # Display items that need restocking
    if need_restock:
        print(emoji.emojize(":warning: PRODUCTS THAT NEED RESTOCKING :warning:"))
        print("━" * 40)
        for product, quantity in need_restock.items():
            print(f"🛒 {product.title()}: Only {quantity} left!")
        print("━" * 40)
        print(emoji.emojize(":check_mark_button: Restock alert sent successfully!"))


store(
    "nails", "hammers", "screws", "paint brushes",  # Separate items for *in_store
    screw_drivers=67,
    cement=50,
    shovels=39
)

def cafe_order(name, *main_drinks, **customized_drinks):
    print(emoji.emojize(":hot_beverage:"*20))
    print(emoji.emojize(f":cherry_blossom: ORDER FOR {name.upper()} :cherry_blossom:"))
    print("_"*40)
    if main_drinks:
        print("DRINKS ORDERED:")
        for i, drinks in enumerate(main_drinks,1):
            print(f"{i}. {drinks.title()}")

    if customized_drinks:
        print(emoji.emojize(":sparkles: CUSTOMIZATIONS :sparkels:"))
        for i, ( drink, customization) in enumerate(customized_drinks.items(),1):
            print(f"\n{i}. {drink.replace('-', '').title()}: {customization}")

cafe_order("EVELYNE", "Latte", "cappuccino", "hot chocolate",
           Latte= "Extra sugar, Whipped Cream",
           Cappuccino = "Double shot, Almond milk",
           Hot_chocolate = "Marshmallows, Extra Chocolate"
           )

print("-"*40)

#Lambda Functions
print(emoji.emojize(":red_heart: ")*18)
square = lambda x : x**2
multiply = lambda x, y:x*y
is_even = lambda x: x%2 ==0
print(f"The square of 5: {square(5)}")
print(f"4 times 6 is {multiply(4,6)}")
print(f"Is 7 even? {is_even(7)}")

shout = lambda name, age: f"My name is {name.upper()}. I am {age} yers old."
print(shout("Evelyne", 19))


compliment = lambda name: f"{name.title()}! That's amazing"
print(compliment("evelyne"))

#Global variables
s = "I love coding"
def fun():
    global s
    s += " GFG"
    print(s)
    s = "Look for a course to pursue online"
    print(s)
fun()
#Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
print("-"*40)
def countdown(n):
    #Base case - when to stop
    if n <=0:
        print("Blast off!")
        return
    #Recursive case - call itself
    print(f"{n}...")
    countdown(n-1) #call itself with n-1

countdown(5)
