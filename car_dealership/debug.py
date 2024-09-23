from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Car, Customer, Sale, Base
from datetime import date


# Set up the database engine and session
engine = create_engine('sqlite:///car_dealership.db')
Session = sessionmaker(bind=engine)
session = Session()

def reset_database():
    #drop existing tables and recreate them
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    #seed data for customers
    customer1 =Customer(name="Elsie Wangui",phone_number="0723561238",email="elsie@gmail.com")
    customer2 =Customer(name="Olivia Waweru",phone_number="0712749027",email="olivia@gmail.com")
    customer3 =Customer(name="Noah Johnson",phone_number="0732678153",email="noah@gmail.com")
    customer4 =Customer(name="Aaron Muhanji",phone_number="0722451732",email="aaron@gmail.com")
    customer5 =Customer(name="Caren Naserian",phone_number="0716729003",email="caren@gmail.com")

    #adding customers to the session
    session.add_all([customer1,customer2,customer3,customer4,customer5])
    session.commit()

    #seed data for cars
    car1 =Car(make="Jaguar", model="F-TYPE", year=2023, price=5700000.0,is_sold=True)
    car2 =Car(make="Honda", model="Civic", year=2019, price=4500000.0,is_sold=False)
    car3 =Car(make="Ford", model="Mustang", year=2021, price=3200000.0,is_sold=False)
    car4 =Car(make="Chevrolet", model="Malibu", year=2022, price=6700000.0,is_sold=False)
    car5 =Car(make="Tesla", model="Model 3", year=2023, price=10900000.0,is_sold=False)
    car6 =Car(make="Land Rover",model="Range Rover Sport",year=2024,price=115000000.0,is_sold=True)

    #dding cars to the session
    session.add_all([car1,car2,car3,car4,car5,car6])
    session.commit()

    #seed data for sales
    sale1 =Sale(car_id=car1.id,customer_id=customer1.id,sale_price=5700000.0,sale_date=date(2023,5,1))
    sale2 =Sale(car_id=car6.id,customer_id=customer3.id,sale_price=115000000.0,sale_date=date(2024,7,24))

    

    #adding sales to the session
    session.add_all([sale1, sale2])
    session.commit()


# Run the reset and seed function
if __name__ == '__main__':
    reset_database()
    
