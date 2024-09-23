# CAR DEALERSHIP MANAGEMENT CLI

This project is a Python-based CLI application for managing car sales, customers, and car inventory. It uses an ORM to interact with a database that stores details of cars, customers, and sales records.


## FEATURES

1.Add new customers,cars and sales

2.Update any information on the cars,customers tables

3,View all customers,cars and sales

4.Delete records of any customers,cars or sales recorded


# REQUIREMENTS

To run this project, you'll need:

  -Python 3.8+
  -Pipenv (for managing dependencies)


## INSTALLATION

Clone this repository:

   git clone git@github.com:Elsiewangui/phase-3-project.git

Navigate to the project directory:

   cd car_dealership

Install the dependencies using Pipenv:

   -pipenv install

Activate the virtual environment:

   -pipenv shell

Seed the default data for the application by running:

   -python debug.py

Run the application:

   -python cli.py


## DEPENDANCIES

SQLAlchemy: ORM for database management.

Pipenv: Used to manage the project's virtual environment and dependencies.


## CLI USAGE

When you run the program, you'll be presented with a main menu offering different options for managing cars, customers, and sales. Here's a breakdown of the features:


## MAIN MENU

**1.Manage Cars**

   -Add new car

   -View all cars

   -Update car Information

   -Delete  car 

   -Back to main menu

**2.Manage Customers**

   -Add a new customer

   -View all customers

   -Update customer Information

   -Delete a customer

   -Back to main menu

**3.Manage Sales**

   -Record a new sale

   -View all sales

   -Delete a sale

   -Back to main menu

**4.Exit the program.**


## FUNCTIONS AND WORKFLOW.

Here are some examples of some functions and workflows:

**main_menu()**

Purpose: Displays the main menu options for managing the system and handles user input.

Workflow:

 -Enters an infinite loop, presenting options to manage cars, customers, sales, or exit

 -Captures user input and directs to the appropriate submenu function based on the choice

 -Validates input, displaying an error message for invalid selections

**manage_cars_menu()**

Purpose: Displays options for managing cars and handles user input for car-related operations.

Workflow:

 -Similar to main_menu, it presents options for adding, viewing, updating, or deleting cars

 -Calls the appropriate function based on user choice

 -Returns to the main menu when the user selects to go back.

**add_new_car()**

Purpose: Collects information to add a new car to the database.

Workflow:

 -Prompts the user for car details (make, model, year, price)

 -Retrieves a new session and creates a Car instance with the provided details

 -Adds the new car to the session, commits the transaction, and closes the session

 -Displays a confirmation message upon success.

**update_car_info()**

Purpose: Allows users to update the details of an existing car.

Workflow:

 -Prompts for the car ID to update and retrieves the corresponding car

 -Asks for new details for make, model, year, and price, allowing blank entries to keep current values

 -Updates the car details if provided and commits changes to the database.

 -Displays success or error messages based on the outcome

**record_sale()**

Purpose: Records a sale transaction between a customer and a car.

Workflow:

 -Prompts for customer ID, car ID, and sale date.

 -Validates the sale date format and checks if the customer and car exist.

 -If the car is sold, displays a warning message and exits.

 -Creates a new Sale instance and updates the car's status to sold.

 -Commits the transaction and confirms the sale.

**view_all_sales()**

Purpose: Retrieves and displays all sales records.

Workflow:

 -Opens a session and queries all Sale records

 -For each sale, retrieves customer details and prints the sale information.

 -Closes the session and waits for user input before returning to the menu.

**update_customer_info()**

Purpose: Allows users to update the details of an existing customer.

Workflow:

 -Prompts for the customer ID to update and retrieves the corresponding customer

 -Asks for new details for name, phone number, and email, allowing blank entries to keep current values

 -Updates the customer details if provided and commits changes to the database.

 -Displays success or error messages based on the outcome

**delete_customer()**

Purpose: Deletes a customer record from the database.

Workflow:

 -Prompts for the customer ID to delete and retrieves the corresponding customer

 -If the customer exists, it deletes the record, commits changes, and confirms the deletion

 -Displays an error message if the customer is not found




## DATA MODEL(models.py)

This project follows an Object-Relational Mapping (ORM) structure with three main models:

**1.Car**

   -Represents a car in the inventory

   -Attributes: id, make, model, year, price, is_sold.

   -Relationships: One-to-One with Sale

**2.Customer**

   -Represents a customer who buys cars.

   -Attributes: id, name, email,phone number

   --Relationships: Many-to-One with Sale

**3.Sale**

   -Represents a sale transaction

   -Attributes: id, customer_id, car_id, sale_date, sale_price

   -Relationships: One-to-One with Car, and One-to-Many with Customer.


