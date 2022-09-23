# Define a property that must have the same value for every class instance (object)

class Gadgets():
    brand = "Samsung"

    def __init__(self, price, color):
        self.price = price
        self.color = color

    def laptop(self):
        print("Laptop is {} brand, Its color is {} & its price {}".format(self.brand, self.color, self.price))

    def cellphone(self):
        print("Cellphone is {} brand, Its color is {} & its price {}".format(self.brand, self.color, self.price))

gadget1 = Gadgets(90000, "Black")
gadget2 = Gadgets(25000, "Grey")

gadget1.laptop()
gadget2.cellphone()

"""
Create Class Vehicle, and inherit the class for creating
	School Bus
	Office Cab
	Truck and
	Tractor

	Use of atleast 4 Instace Variables and 2 Class Variables and 3 Methods
"""

class Vehicle():
    manufacturer = "BharatBenz"
    fuel = "Diesel"

    def __init__(self, seat_color, no_of_seats, driver_name, vehicle_no):
        self.seat_color = seat_color
        self.no_of_seats = no_of_seats
        self.driver_name = driver_name
        self.vehicle_no = vehicle_no

class Transporation(Vehicle):
    def school_bus(self):
        print("School bus is manufactured by {}, its {} vehicle, seat color is {} , no of seats is {}, driver name is {} & vehicle no is {}"
              .format(self.manufacturer, self.fuel, self.seat_color, self.no_of_seats, self.driver_name, self.vehicle_no))

    def office_cab(self):
        print("Office cab is manufactured by {}, its {} vehicle, seat color is {} , no of seats is {}, driver name is {} & vehicle no is {}"
              .format(self.manufacturer, self.fuel, self.seat_color, self.no_of_seats, self.driver_name, self.vehicle_no))

    def tractor(self):
        print("Tractor is manufactured by {}, its {} vehicle, seat color is {} , no of seats is {}, driver name is {} & vehicle no is {}"
              .format(self.manufacturer, self.fuel, self.seat_color, self.no_of_seats, self.driver_name, self.vehicle_no))

    def truck(self):
        print("Truck is manufactured by {}, its {} vehicle, seat color is {} , no of seats is {}, driver name is {} & vehicle no is {}"
              .format(self.manufacturer, self.fuel, self.seat_color, self.no_of_seats, self.driver_name, self.vehicle_no))

obj1 = Transporation("black", 45, "Ramu", 6014)
obj2 = Transporation("blue", 20, "laxman", 5012)
obj3 = Transporation("white", 2, "manoj", 2012)
obj4 = Transporation("grey", 6, "yash", 1021)

obj1.school_bus()
obj2.office_cab()
obj3.tractor()
obj4.truck()



