from database_setups import save_to_database, retrieve_from_database
from product import get_a_product, reduce_product_qty_by_qty_requested
from utils import generate_random_number_for_id


def retrieve_requests_from_database():
    return retrieve_from_database('requests.json')


# Retrieve the request data from the database
Requests = retrieve_requests_from_database()


def get_a_request(id):
    for request in Requests:
        if request.get('id') == id:
            return request
    return False


# Request a product or item
def request_for_a_product(customer):
    product_name_sku = input("Enter product name or sku/ID: ")

    # Checking if product exists, to prevent requesting product which is not in the database
    product = get_a_product(product_name_sku)
    if (not product):
        print("We currently don't have this product with the name or sku of " +
              product_name_sku)
        return

    qty_requested = int(input("Enter quantity to request: "))

    # Prevent requesting for quantities higher than what is currently available for the product
    if (product['qty'] < qty_requested):
        print("You can't request for " + str(qty_requested) +
              " quantities, we have only " + str(product['qty']) + " left")
        return

    # Removing the customer/user password and product qty before saving the request
    customer.pop("password", None)
    product.pop("qty", None)

    new_request = {
        "id": "req-"+generate_random_number_for_id(),
        "product": product,
        "qty_requested": qty_requested,
        "status": 'pending',
        "customer": customer,
    }

    Requests.append(new_request)
    save_to_database(Requests, 'requests.json')
    print("Requests added.")


def approve_or_decline_a_request():
    id = input("Enter request id: ")

    # Checking if request exists
    request = get_a_request(id)
    if (not request):
        print("No request with the id of " +
              id)
        return

    request_options = """
    Request options:
    1. Approve request
    2. Decline request
    """

    print(request_options)

    choice = int(input("Enter your request option: "))

    if choice == 1:
        if request['status'] == 'approved':
            print('This request has been approved already')
            return
        request['status'] = 'approved'
        reduce_product_qty_by_qty_requested(
            request['product']['sku'],  request['qty_requested'])
    elif choice == 2:
        request['status'] = 'declined'
    else:
        print("Invalid choice. Please enter a valid option (1-2).")

    save_to_database(Requests, 'requests.json')
    if request['status'] == 'approved':
        print("Request approved.")
    if request['status'] == 'declined':
        print("Request declined.")


def view_requests(logged_in_user):
    message = """
        Below are the requests
            
        """
    if Requests:
        is_manager = logged_in_user['role'] == 'Manager'
        is_customer = logged_in_user['role'] == 'Customer'
        customer_username = logged_in_user['username']

        def display_request(request):
            print("Request ID:", request['id'])
            print("Qty requested:", request['qty_requested'])
            print("Status:", request['status'])
            print("Product:", request['product']['name'])
            print("Customer:", request['customer']['name'])
            print()

        view_options = """
                View options:
                1. Prending requests
                2. Approved requests
                3. Decline requests
                4. All requests
                5. Exist requests
                """

        print(view_options)

        choice = int(input("Enter your option: "))

        print(message)

        found = False
        for request in Requests:
            while True:
                if choice == 1:
                    if is_manager and request['status'] == 'pending':
                        display_request(request)
                        found = True

                    if is_customer and request['status'] == 'pending' and request['customer']['username'] == customer_username:
                        display_request(request)
                        found = True

                elif choice == 2:
                    if is_manager and request['status'] == 'approved':
                        display_request(request)
                        found = True

                    if is_customer and request['status'] == 'approved' and request['customer']['username'] == customer_username:
                        display_request(request)
                        found = True

                elif choice == 3:
                    if is_manager and request['status'] == 'declined':
                        display_request(request)
                        found = True

                    if is_customer and request['status'] == 'declined' and request['customer']['username'] == customer_username:
                        display_request(request)
                        found = True

                elif choice == 4:
                    if is_manager:
                        display_request(request)
                        found = True

                    if is_customer and request['customer']['username'] == customer_username:
                        display_request(request)
                        found = True

                elif choice == 5:
                    print("Exiting requests")
                    break
                else:
                    print("Invalid choice. Please enter a valid option (1-5).")

        if not found:
            print("No request found")
    else:
        print("No request found in the database.")
