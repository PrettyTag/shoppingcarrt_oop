import csv

class Product:
    def __init__(self, name, price, category):
        """
        Initializes a new Product instance.

        :param name: The name of the product.
        :param price: The price of the product.
        :param category: The category of the product.
        """
        self.name = name
        self.price = price
        self.category = category
        self.save_to_csv()

    def save_to_csv(self, filename='products.csv'):
        """
        Saves the product information to a CSV file.

        :param filename: The name of the CSV file to save to (default is 'products.csv').
        """
        try:
            # Open the CSV file in write mode
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)

                # Write the header if the file is empty
                if file.tell() == 0:
                    writer.writerow(['Name', 'Price', 'Category'])

                # Write the product information
                writer.writerow([self.name, self.price, self.category])

            print(f"Product '{self.name}' saved to {filename} successfully.")
        except Exception as e:
            print(f"Error saving product to {filename}: {e}")
