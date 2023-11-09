from product import Product

class ShoppingCart:
    def __init__(self):
        """
        Initializes a new ShoppingCart instance.
        """
        self.products = []
        self.cart_cost = 0

    def calculate_cart_cost(self):
        """
        Calculates the total cost of all products in the shopping cart.
        """
        self.cart_cost = 0  # Reset cart_cost before recalculating
        for item in self.products:
            self.cart_cost += item.price

    def add_to_cart(self, product):
        """
        Adds a product to the shopping cart.

        :param product: The product to be added to the cart.
        """
        self.products.append(product)

    def empty_cart(self):
        """
        Empties the shopping cart and resets the cart cost to zero.
        """
        self.products.clear()
        self.cart_cost = 0
