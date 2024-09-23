from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,Float,Boolean,Date
from sqlalchemy.orm import relationship


engine =create_engine('sqlite:///car_dealership.db')

Base=declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    
    id =Column(Integer, primary_key=True)
    make =Column(String)
    model =Column(String)
    year =Column(Integer)
    price =Column(Float)
    is_sold =Column(Boolean,default=False)#indicates whether the ca has been sold or not

    
    #relationship to Sale (One-to-One)
    sale =relationship('Sale',uselist=False,back_populates='car')
    

    def __repr__(self):
        return f"<Car(make={self.make}, model={self.model}, year={self.year})>"
    

class Sale(Base):
    __tablename__ = 'sales'
    
    id =Column(Integer, primary_key=True)
    car_id =Column(Integer, ForeignKey('cars.id'))
    customer_id =Column(Integer, ForeignKey('customers.id'))
    sale_price =Column(Float)
    sale_date =Column(Date,nullable=True)
    
    #relationship to Car (One-to-One)
    car =relationship('Car', back_populates='sale')
    
    #relationship to Customer (Many-to-One)
    customer =relationship('Customer', back_populates='sales')

    def __repr__(self):
        return f"<Sale(car_id={self.car_id}, customer_id={self.customer_id}, price={self.sale_price})>"
    


class Customer(Base):
    __tablename__ = 'customers'
    
    id =Column(Integer, primary_key=True)
    name =Column(String)
    phone_number =Column(String)
    email =Column(String)
    
    #relationship to Sales (One-to-Many)
    sales =relationship('Sale', back_populates='customer')
    

    def __repr__(self):
        return f"<Customer(name={self.name}, email={self.email})>"