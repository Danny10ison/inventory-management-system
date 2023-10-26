import random
from database_setups import save_to_database, retrieve_from_database


# A function check if product already exists
def product_already_exists(product_list, name):
    for product in product_list:
        if product.get('name') == name:
            return True
    return False


def retrieve_products_from_database():
    return retrieve_from_database('products.json')


def add_product():

    Products = retrieve_products_from_database()

    # sku = "prod-"+str(random_number)
    name = input("Enter product name: ")

    if product_already_exists(Products, name):
        print("You are already added this product")
        return

    shelf_life = input("Enter product shelf life (yyyy-mm-dd): ")
    volume = input("Enter product volume (E.g 5ml): ")
    qty = float(input("Enter product qty in stock: "))
    price = float(input("Enter product price: "))

    # Generate a random 5-digit number
    random_number = random.randint(10000, 99999)
    sku = "prod-"+str(random_number)

    new_product = {
        "sku": sku,
        "name": name,
        "shelf_life": shelf_life,
        "volume": volume,
        "qty": qty,
        "price": price,
    }

    Products.append(new_product)
    save_to_database(Products, 'products.json')
    print("Product added.")


def view_products():
    products = retrieve_products_from_database()

    message = """

    Below are the products available
        
    """
    if products:

        print(message)

        for product in products:
            print("SKU/ID:", product['sku'])
            print("Name:", product['name'])
            print("Shelf Life:", product['shelf_life'])
            print("Volume:", product['volume'])
            print("Quantity:", product['qty'])
            print("Price:", product['price'])
            print()
    else:
        print("No products/items found in the database.")
