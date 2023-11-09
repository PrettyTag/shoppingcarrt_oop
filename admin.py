import csv
from datetime import datetime
from product import Product

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


def add_product_to_system():
    """
    Adds a new product to the system.
    """
    print("======= New product ==========")
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_category = input("Enter product category: ")

    new_product = Product(product_name, product_price, product_category)

    try:
        # Open the CSV file in append mode and write the new product
        with open('products.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write the header if the file is empty
            if file.tell() == 0:
                writer.writerow(['Name', 'Price', 'Category'])

            # Write the new product information
            writer.writerow([new_product.name, new_product.price, new_product.category])

        print(f"Product '{new_product.name}' added to the system successfully.")
        print("=================================")
    except Exception as e:
        print(f"Error adding product to the system: {e}")

def track_daily_sales():
    """
    Tracks daily sales and saves them to a CSV file.
    """
    try:
        # Open the CSV file in append mode and write the daily sales
        with open('daily_sales.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write the header if the file is empty
            if file.tell() == 0:
                writer.writerow(['Date', 'Total Sales'])

            # Write the daily sales information
            date = datetime.now().strftime('%Y-%m-%d')
            total_sales = calculate_total_sales()
            writer.writerow([date, total_sales])

        print(f"Daily sales tracked successfully.")
    except Exception as e:
        print(f"Error tracking daily sales: {e}")

def calculate_total_sales():
    """
    Calculates the total sales for the day.
    """
    today_date = datetime.now().strftime('%Y%m%d')
    total_sales = 0

    try:
        with open('sales.csv', mode='r') as file:
            reader = csv.reader(file)

            # Skipping header row
            next(reader, None)

            for row in reader:
                sale_id = row[0]
                sale_date = sale_id[:8]  # Extract the first 8 characters as the date part of sale_id

                if sale_date == today_date:
                    total_sales += float(row[2])  # total price is in the third column

    except Exception as e:
        print(f"Error calculating total sales: {e}")

    return total_sales

def view_sale_details(sale_id):
    """
    Views details of a specific sale.
    """
    try:
        # Open the CSV file in read mode and display sale details
        with open('sales.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == sale_id:  # sale_id is in the first column
                    # print("=================================")
                    print(f"Sale ID: {row[0]}")
                    print(f"Customer Name: {row[1]}")
                    print(f"Total Price: {row[2]}")
                    print(f"Cart ID: {row[3]}")
                    

        print(f"Sale details for Sale ID {sale_id}.")
        print("=================================")
    except Exception as e:
        print(f"Error viewing sale details: {e}")

if __name__ == "__main__":
    print("Welcome to the Admin Panel")

    while True:
        print("============== Menu ===================")
        print("1. Add Product to System")
        print("2. Track Daily Sales")
        print("3. View Sale Details")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product_to_system()
        elif choice == '2':
            track_daily_sales()
        elif choice == '3':
            print("=================================")
            sale_id = input("Enter Sale ID to view details: ")
            view_sale_details(sale_id)
        elif choice == '0':
            print("=================================")
            print("=================================")
            print("Exiting Admin Panel. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1, 2, 3, or 0).")
