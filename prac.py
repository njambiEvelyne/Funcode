import emoji

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
        print(emoji.emojize(":sparkles: CUSTOMIZATIONS"))
        for drink, customization in enumerate(customized_drinks.items(), 1):
            print(f"\n{drink}: {customization}")n




cafe_order("EVELYNE", "Latte", "cappuccino", "hot chocolate",
           Lette= "Extra sugar, Whipped Cream",
           Cappuccino = "Double shot, Almond milk",
           Hot_chocolate = "Marshmallows, Extra Chocolate"
           )