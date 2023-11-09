from shoppingcart import ShoppingCart
import csv
from datetime import datetime


class Customer:
    def __init__(self, name):
        """
        Initializes a new Customer instance.

        :param name: The name of the customer.
        """
        self.name = name
        self.cart = ShoppingCart()

    def add_item_to_cart(self, product):
        """
        Adds a product to the customer's shopping cart.

        :param product: The product to be added to the cart.
        """
        self.cart.add_to_cart(product)

    def view_cart(self):
        """
        Displays the contents of the customer's shopping cart.
        """
        if len(self.cart.products) == 0:
            print("Your cart is empty :(")
        else:
            for item in self.cart.products:
                print(item.name)

    def save_cart_to_file(self, filename='customer_cart.csv', sales_filename='sales.csv'):
        """
        Saves the customer's information and cart items to a CSV file.

        :param filename: The name of the CSV file to save cart items to (default is 'customer_cart.csv').
        :param sales_filename: The name of the CSV file to save sales information to (default is 'sales.csv').
        """
        try:
            # Generate a sale_id based on the current timestamp
            sale_id = datetime.now().strftime('%Y%m%d%H%M%S')

            # Open the cart CSV file in write mode
            with open(filename, mode='a', newline='') as cart_file:
                cart_writer = csv.writer(cart_file)

                # Write the header if the file is empty
                if cart_file.tell() == 0:
                    cart_writer.writerow(['Sale ID', 'Customer Name', 'Product Name', 'Price', 'Category', 'Cart ID'])

                # Write customer and cart information
                for item in self.cart.products:
                    cart_writer.writerow([sale_id, self.name, item.name, item.price, item.category, self.cart.cart_id])

            # Open the sales CSV file in append mode
            with open(sales_filename, mode='a', newline='') as sales_file:
                sales_writer = csv.writer(sales_file)

                # Write the header if the file is empty
                if sales_file.tell() == 0:
                    sales_writer.writerow(['Sale ID', 'Customer Name', 'Total Price', 'Cart ID'])

                # Write sales information
                total_price = sum(item.price for item in self.cart.products)
                sales_writer.writerow([sale_id, self.name, total_price, self.cart.cart_id])

            print(f"Customer '{self.name}' and cart items saved to {filename} successfully.")
        except Exception as e:
            print(f"Error saving customer and cart items to {filename}: {e}")