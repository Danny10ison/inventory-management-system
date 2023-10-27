from database_setups import save_to_database, retrieve_from_database
from utils import generate_random_number_for_id


def retrieve_products_from_database():
    return retrieve_from_database('products.json')


Products = retrieve_products_from_database()


# A function to get a product by name or sku
def get_a_product(name_sku):
    for product in Products:
        if product.get('name') == name_sku:
            return product
        if product.get('sku') == name_sku:
            return product
    return False


def reduce_product_qty_by_qty_requested(name_sku, qty_requested):
    product = get_a_product(name_sku)
    product['qty'] = product['qty'] - qty_requested
    save_to_database(Products, 'products.json')


def add_product():

    # sku = "prod-"+str(random_number)
    name = input("Enter product name: ")

    # check if product already exists
    if get_a_product(name):
        print("You are already added this product")
        return

    shelf_life = input("Enter product shelf life (yyyy-mm-dd): ")
    volume = input("Enter product volume (E.g 5ml): ")
    qty = float(input("Enter product qty in stock: "))
    price = float(input("Enter product price: "))

    sku = "prod-"+generate_random_number_for_id()

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


def view_single_product():
    name_sku = input("Enter product name or sku/ID: ")
    product = get_a_product(name_sku)

    message = """

    Below is the information of the product

    """

    if (product):

        print(message)

        print("SKU/ID:", product['sku'])
        print("Name:", product['name'])
        print("Shelf Life:", product['shelf_life'])
        print("Volume:", product['volume'])
        print("Quantity:", product['qty'])
        print("Price:", product['price'])
        print()
    else:
        print("No product with the name or sku of " + name_sku + " found")
