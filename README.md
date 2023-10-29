# inventory-management-system
CLI based Inventory Management System

## Requirements

Inventory Management System - Console App

Interface - Terminal / Console

Users
 
 - Customer
 - Inventory Manager
	
Product:
 
 - Bottled Water (different sizes)
	
 	
Specs Product

Product Name
 
 - SKU / ID
 - Shelf life
 - Volume
 - Add product / Restock
	
Manager specs
 
 - Full name
 - User name
 - Password
	
Customer specs
 
 - Fullname
 - User name
 - Password
	
Inventory Manager can
	View all products available
	Add product or restock
	View Inventory requests
	Accept / Deny Requests
	
Customer can
	make request of product
	
## App Flow


1. Welcome and Login Screen to login as manager or customer

- Manager login
- User Login
- Close the App
- How to use the app (optional)
	
3. Manager home screen 

- view all available products
- add products
- view request
- approve request
- add customer
- view all transactions (optional)
- back to Page 1 or 
- exit app directly /log out
	
4. Customer home screen

- make product request
- view request status
- view all transactions (optional)
- back to Page 1 or
- exit app directly / log out


## Usage 

###  Ubuntu 22.04

1. Open your terminal

2. Change your current directory (folder) to the "Desktop" folder.
   ```bash
   cd Desktop
   ```

3. Clone the project
   ```bash
   git clone https://github.com/Danny10ison/inventory-management-system.git
   ```
   This line clones a Git repository from GitHub. It creates a copy of the "inventory-management-system" repository from the specified URL and stores it on your local machine.

4. After cloning the repository, change your current directory to the project repository
   ```bash
   cd inventory-management-system/
   ```

5. Open the project within Visual Studio code. It allows you to start working on the code within the repository.
   ```bash
   code .
   ```
6. Launch your VSCode terminal

7. Run the script associated with the inventory management system
   ```bash
   python3 app.py
   ```

> Ubuntu 22.04 Usage guide by: Azumah Joshua :sunglasses:
