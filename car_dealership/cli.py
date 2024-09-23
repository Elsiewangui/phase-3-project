import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Car, Sale,Customer
from datetime import datetime




def get_session():
    engine = create_engine('sqlite:///car_dealership.db')

    Session = sessionmaker(bind=engine)
    return Session()



#main menu for managing the sytdtem
def main_menu():
    while True:
        print("1.Manage Cars")
        print("2.Manage Customers")
        print("3.Manage Sales")
        print("4.Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            manage_cars_menu()
        elif choice == '2':
            manage_customers_menu()
        elif choice == '3':
            manage_sales_menu()
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid choice.Please try again.")

#menu for managing cars
def manage_cars_menu():
    while True:
        print("1.Add New Car")
        print("2.View All Cars")
        print("3.Update Car Information")
        print("4.Delete Car")
        print("5.Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            add_new_car()
        elif choice == '2':
            view_all_cars()
        elif choice == '3':
            update_car_info()
        elif choice == '4':
            delete_car()
        elif choice == '5':
            return
        else:
            print("Invalid choice.Please try again.")

#menu for managing customers
def manage_customers_menu():
    while True:
        print("1.Add New Customer")
        print("2.View All Customers")
        print("3.Update Customer Info")
        print("4.Delete Customer")
        print("5.Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            add_new_customer()
        elif choice == '2':
            view_all_customers()
        elif choice == '3':
            update_customer_info()
        elif choice == '4':
            delete_customer()
        elif choice == '5':
            return
        else:
            print("Invalid choice.Please try again.")

#menu for manging sales
def manage_sales_menu():
    while True:
        print("1.Record a Sale")
        print("2.View All Sales")
        print("3.Delete a Sale")
        print("4.Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            record_sale()
        elif choice == '2':
            view_all_sales()
        elif choice == '3':
            delete_sale()
        elif choice == '4':
            return
        else:
            print("Invalid choice.Please try again.")

#function to add a new car
def add_new_car():
    make =input("Enter car make: ")
    model =input("Enter car model: ")
    year =int(input("Enter car year: "))
    price =float(input("Enter car price: "))

    session = get_session()#session for interacting with the database
    new_car =Car(make=make,model=model,year=year,price=price)#create a new car intance
    session.add(new_car)#add the new car to the session
    session.commit()#commit the transaction ,saving the car to the databse
    session.close()#close the session

    print(f"Added car: {make} {model} ({year}) - ${price}")
    input("Press Enter to return to the menu...")

#function to view all cars
def view_all_cars():
    session =get_session()
    cars =session.query(Car).all()
    session.close()

    for car in cars:#loop through every car and display it
        print(f"{car.id}: {car.make} {car.model} ({car.year}) - ${car.price}")

    input("Press Enter to return to the menu...")

#function to update car info
def update_car_info():
    car_id =int(input("Enter car ID to update: "))
    new_make =input("Enter new make (leave blank to keep current): ")
    new_model =input("Enter new model (leave blank to keep current): ")
    new_year =input("Enter new year (leave blank to keep current): ")
    new_price =input("Enter new price (leave blank to keep current): ")

    session =get_session()
    car =session.query(Car).filter_by(id=car_id).first()

    if car:
        #update the car if any new information has been updated
        if new_make:
            car.make =new_make
        if new_model:
            car.model =new_model
        if new_year:
            car.year =int(new_year)
        if new_price:
            car.price =float(new_price)

        session.commit()
        print(f"Updated car ID {car_id}.")
    else:
        print("Car not found.")
    
    session.close()
    input("Press Enter to return to the menu...")

#function to delete car
def delete_car():
    car_id =int(input("Enter car ID to delete: "))

    session =get_session()
    car =session.query(Car).filter_by(id=car_id).first()#query the car by ID

    if car:
        session.delete(car)
        session.commit()
        print(f"Deleted car ID {car_id}.")
    else:
        print("Car not found.")
    
    session.close()
    input("Press Enter to return to the menu...")

#function add a new customer
def add_new_customer():
    name =input("Enter customer name: ")
    phone_number=int(input("Enter customer phonenumber: "))
    email =input("Enter customer email: ")

    session =get_session()
    new_customer = Customer(name=name,email=email, phone_number=phone_number)
    session.add(new_customer)
    session.commit()
    session.close()

    print(f"Added customer: {name} {email} {phone_number}")
    input("Press Enter to return to the menu...")

#function to view all customers
def view_all_customers():
    session = get_session()
    customers = session.query(Customer).all()
    session.close()

    for customer in customers:
        print(f"{customer.id}: {customer.name} {customer.email} {customer.phone_number}")

    input("Press Enter to return to the menu...")

#function update customer info
def update_customer_info():
    customer_id =input("Enter customer ID to update: ")
    session=get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        print("Customer not found.")
        return

    new_name =input("Enter new name (leave blank to keep current): ")
    if new_name:
        customer.name =new_name

    new_phonenumber =input("Enter new phonenumber (leave blank to keep current): ")
    if new_phonenumber:  #check if the input is not blank
        customer.phone_number =new_phonenumber  

    new_email =input("Enter new email (leave blank to keep current): ")
    if new_email:
        customer.email =new_email

    session.commit()
    print(f"Updated customer: {customer.name} {customer.email} {customer.phone_number}")

#function delete customer
def delete_customer():
    customer_id =int(input("Enter customer ID to delete: "))

    session =get_session()
    customer =session.query(Customer).filter_by(id=customer_id).first()

    if customer:
        session.delete(customer)
        session.commit()
        print(f"Deleted customer ID {customer_id}.")
    else:
        print("Customer not found.")
    
    session.close()
    input("Press Enter to return to the menu...")

#function record a new sale
def record_sale():
    customer_id = int(input("Enter customer ID: "))
    car_id = int(input("Enter car ID: "))

    #loops until a valid date is entered
    while True:
        sale_date_input = input("Enter sale date (YYYY-MM-DD): ")
        try:
            #converts the string to a date object
            sale_date = datetime.strptime(sale_date_input, '%Y-%m-%d').date()
            break  #exits loop if the date is valid
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")

    session =get_session()

    #retrieves the customer and car from the database
    customer = session.query(Customer).filter_by(id=customer_id).first()
    car = session.query(Car).filter_by(id=car_id).first()

    if customer and car:
        #checks if the car is already sold
        if car.is_sold:
            print("This car has already been sold.")
            session.close()
            return
        
        #creates a new sale record
        sale_price = car.price  # Automatically use the car's price
        new_sale = Sale(customer_id=customer_id, car_id=car_id, sale_date=sale_date, sale_price=sale_price)
        
        #adds the new sale to the session
        session.add(new_sale)

        #marks the car as sold in the car table
        car.is_sold = True
        
        #commit the transaction
        session.commit()

        print(f"Recorded sale: Customer ID {customer_id}, Car ID {car_id}, Sale Date {sale_date}, Price {sale_price}")
    else:
        print("Customer or Car not found.")
    
    session.close()
    input("Press Enter to return to the menu...")



#function view all sales
def view_all_sales():
    session =get_session()
    sales =session.query(Sale).all()

    for sale in sales:
        customer =session.query(Customer).filter_by(id=sale.customer_id).first()
        print(f"Sale ID {sale.id}: Customer ID {sale.customer_id},Car ID {sale.car_id},Date {sale.sale_date},Price {sale.sale_price}")

    session.close()
    input("Press Enter to return to the menu...")

#function delete sale record
def delete_sale():
    sale_id = int(input("Enter sale ID to delete: "))#get sale ID from user
    session = get_session()
    
    #retrieve the sale record
    sale = session.query(Sale).filter_by(id=sale_id).first()
    
    if sale:
        #get the car
        car = session.query(Car).filter_by(id=sale.car_id).first()
        if car:
            #check if there are any other sales for this car
            other_sales = session.query(Sale).filter(Sale.car_id == car.id).count()
            if other_sales == 1:  # This is the only sale for the car
                car.is_sold = False  # Mark the car as unsold
        
        #deletes the sale record
        session.delete(sale)

        #commit the changes to the database
        session.commit()
        print(f"Deleted sale with ID: {sale_id}. The car is now marked as unsold.")
    else:
        print("Sale not found.")

    session.close()
    input("Press Enter to return to the menu...")

if __name__ == '__main__':
    main_menu()