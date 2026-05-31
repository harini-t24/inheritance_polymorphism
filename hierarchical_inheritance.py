class Vehicle:
    def getdetails(self):
        self.make = input("Enter Make:")
        self.year = int(input("Enter year:"))
        self.color = input("Enter colour:")

    def display_info(self):
        print("Make of the vehicle:", self.make)
        print("Year :", self.year)
        print("Colour of the vehicle:", self.color)


class car(Vehicle):
    def getcar_details(self):
        self.model = input("Enter model of the car:")
        self.capacity = int(input("Enter capacity:"))

    def display_car(self):
        print("Model of Car:", self.model)
        print("Capacity:", self.capacity)


class bike(Vehicle):
    def getbike_details(self):
        self.type = input("Enter bike type:")
        self.mileage = int(input("Enter mileage:"))

    def display_bike(self):
        print("Model of bike:", self.type)
        print("Mileage of bike:", self.mileage)


print("1.Car\n2.Bike")
c = int(input("Enter your choice of vehicle:"))
if c == 1:
    c = car()
    c.getdetails()
    c.getcar_details()
    c.display_info()
    c.display_car()
elif c == 2:
    b = bike()
    b.getdetails()
    b.getbike_details()
    b.display_info()
    b.display_bike()

else:
    print("Invalid choice")
