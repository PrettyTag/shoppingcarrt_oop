import csv
from customer import Customer
from product import Product
from shoppingcart import ShoppingCart

def load_products_from_csv(filename='products.csv'):
    products = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(row['Name'], float(row['Price']), row['Category'])
                products.append(product)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return products

def display_menu(products):
    print("------ Menu ------")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name} - ${product.price:.2f} ({product.category})")
    print("0. Exit")

def select_product(products):
    while True:
        try:
            choice = int(input("Enter the number of the product to add to the cart (0 to exit): "))
            if 0 <= choice <= len(products):
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and", len(products))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Load products from CSV
all_products = load_products_from_csv()

# Get user's name
user_name = input("Enter your name: ")

# Create a customer with the provided name
customer = Customer(user_name)

while True:
    display_menu(all_products)

    # Get user's choice
    choice = input("Enter your choice (-1 to exit, 0 to confirm checkout): ")

    if choice == '-1':
        # Exit the program
        print("Exiting program. Thank you!")
        break
    elif choice.isdigit() and 1 <= int(choice) <= len(all_products):
        # Add product to cart
        selected_product_index = int(choice)
        selected_product = all_products[selected_product_index - 1]
        customer.add_item_to_cart(selected_product)
        print(f"{selected_product.name} added to the cart.")
    elif choice == '0':
        # Confirm checkout
        print("------ Checkout Summary ------")
        customer.view_cart()
        customer.cart.calculate_cart_cost()
        print(f"Total cost: ${customer.cart.cart_cost:.2f}")    
        
        confirm = input("Do you want to confirm the checkout? (yes/no): ").lower()
        if confirm == 'yes' or confirm == 'y':
            customer.save_cart_to_file()
            print("Checkout confirmed. Thank you!")
            break
        else:
            print("Checkout canceled.")
            customer.cart.empty_cart()
    else:
        print("Invalid choice. Please enter a valid number, 0, or 9.")