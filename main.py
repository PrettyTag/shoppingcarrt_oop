# Importing necessary classes from respective modules
from customer import Customer
from product import Product
from shoppingcart import ShoppingCart

# Creating a customer named 'Tagaya'
customer = Customer('Tagaya')

# Creating instances of products
banana = Product("Bananas", 3.89, "produce")
orange = Product("Oranges", 1.85, "produce")
pineapple = Product("Pineapple", 2.57, "produce")
dogfood = Product("Purina", 18.99, "petfood")

# Printing the customer's name
print(customer.name)

# Adding products to the customer's shopping cart
customer.add_item_to_cart(banana)
customer.add_item_to_cart(orange)
customer.add_item_to_cart(pineapple)
customer.add_item_to_cart(dogfood)

# Calculating the total cost of the items in the cart
customer.cart.calculate_cart_cost()
total_cost = customer.cart.cart_cost

# Printing the total cost
print(total_cost)

# Emptying the shopping cart
customer.cart.empty_cart()

# Viewing the contents of the empty cart
customer.view_cart()
