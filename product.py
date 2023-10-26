import random
from database_setups import save_to_database, retrieve_from_database


# A function check if product already exists
def product_already_exists(product_list, name):
    for product in product_list:
        if product.get('name') == name:
            return True
    return False


def add_product():
    Products = []

    try:
        Products = retrieve_from_database('products.json')
    except FileNotFoundError:
        pass

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


while True:
    print("Options:")
    print("1. Add a new product")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_product()
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")
