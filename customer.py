from shoppingcart import ShoppingCart
import csv

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

    def save_cart_to_file(self, filename='customer_cart.csv'):
        """
        Saves the customer's information and cart items to a CSV file.

        :param filename: The name of the CSV file to save to (default is 'customer_cart.csv').
        """
        try:
            # Open the CSV file in write mode
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)

                # Write the header if the file is empty
                if file.tell() == 0:
                    writer.writerow(['Customer Name', 'Product Name', 'Price', 'Category'])

                # Write customer and cart information
                for item in self.cart.products:
                    writer.writerow([self.name, item.name, item.price, item.category])

            print(f"Customer '{self.name}' and cart items saved to {filename} successfully.")
        except Exception as e:
            print(f"Error saving customer and cart items to {filename}: {e}")
