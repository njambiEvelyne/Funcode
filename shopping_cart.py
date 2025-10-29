class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity} = ${self.get_total_price():.2f}"

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        """Add an item to the cart or update quantity if it already exists"""
        for item in self.items:
            if item.name.lower() == name.lower():
                item.quantity += quantity
                print(f"Updated {name} quantity to {item.quantity}")
                return
        
        # If item doesn't exist, add new product
        new_product = Product(name, price, quantity)
        self.items.append(new_product)
        print(f"Added {quantity} x {name} to cart")
    
    def remove_item(self, name, quantity=None):
        """Remove an item completely or reduce quantity"""
        for i, item in enumerate(self.items):
            if item.name.lower() == name.lower():
                if quantity is None or quantity >= item.quantity:
                    # Remove the entire item
                    removed_item = self.items.pop(i)
                    print(f"Removed {removed_item.name} from cart")
                    return True
                else:
                    # Reduce quantity
                    item.quantity -= quantity
                    print(f"Reduced {name} quantity to {item.quantity}")
                    return True
        
        print(f"Item '{name}' not found in cart")
        return False
    
    def calculate_total(self):
        """Calculate the total price of all items in cart"""
        total = sum(item.get_total_price() for item in self.items)
        return total
    
    def display_cart(self):
        """Display all items in the cart"""
        if not self.items:
            print("Your shopping cart is empty!")
            return
        
        print("\n--- Your Shopping Cart ---")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print(f"Total: ${self.calculate_total():.2f}")
        print("-" * 30)
    
    def generate_receipt(self):
        """Generate a formatted receipt"""
        if not self.items:
            print("Cannot generate receipt - cart is empty!")
            return
        
        print("\n" + "=" * 40)
        print("           RECEIPT")
        print("=" * 40)
        
        for item in self.items:
            print(f"{item.name:<20} ${item.price:>6.2f} x {item.quantity:>2} = ${item.get_total_price():>6.2f}")
        
        print("-" * 40)
        total = self.calculate_total()
        print(f"{'TOTAL:':<20} ${total:>6.2f}")
        print("=" * 40)
        print("Thank you for shopping with us!")
        print("=" * 40)

def main():
    cart = ShoppingCart()
    
    # Sample products for demonstration
    sample_products = {
        "1": {"name": "Pizza", "price": 12.00},
        "2": {"name": "Burger", "price": 8.50},
        "3": {"name": "Salad", "price": 6.75},
        "4": {"name": "Coffee", "price": 3.50},
        "5": {"name": "Cake", "price": 5.25}
    }
    
    while True:
        print("\n=== SHOPPING CART SYSTEM ===")
        print("1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Calculate Total")
        print("5. Generate Receipt")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            cart.display_cart()
        
        elif choice == "2":
            print("\nAvailable products:")
            for key, product in sample_products.items():
                print(f"{key}. {product['name']} - ${product['price']:.2f}")
            
            product_choice = input("\nEnter product number or type product name: ").strip()
            
            if product_choice in sample_products:
                product = sample_products[product_choice]
                name = product["name"]
                price = product["price"]
            else:
                name = product_choice
                try:
                    price = float(input(f"Enter price for {name}: $"))
                except ValueError:
                    print("Invalid price! Using $0.00")
                    price = 0.0
            
            try:
                quantity = int(input(f"Enter quantity for {name}: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
            except ValueError:
                print("Invalid quantity! Using 1")
                quantity = 1
            
            cart.add_item(name, price, quantity)
        
        elif choice == "3":
            if not cart.items:
                print("Cart is empty! Nothing to remove.")
                continue
            
            cart.display_cart()
            item_name = input("Enter the name of item to remove: ").strip()
            
            remove_all = input("Remove all of this item? (y/n): ").strip().lower()
            if remove_all == 'y':
                cart.remove_item(item_name)
            else:
                try:
                    quantity = int(input("Enter quantity to remove: "))
                    if quantity <= 0:
                        print("Quantity must be positive!")
                        continue
                    cart.remove_item(item_name, quantity)
                except ValueError:
                    print("Invalid quantity!")
        
        elif choice == "4":
            total = cart.calculate_total()
            print(f"\nTotal cart value: ${total:.2f}")
        
        elif choice == "5":
            cart.generate_receipt()
        
        elif choice == "6":
            print("Thank you for using the shopping cart system!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-6.")

# Run the program
if __name__ == "__main__":
    main()

  
  
    