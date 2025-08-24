
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"The {self.year} {self.brand} {self.model} has been driven for {miles} miles.")

    def describe_vehicle(self):
        print(f"This vehicle is a {self.year} {self.brand} {self.model} with {self.mileage} miles.")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def describe_vehicle(self):
        super().describe_vehicle()
        print(f"It is a car with {self.doors} doors.")

# Create a Car object
my_car = Car('Toyota', 'Corolla', 2015, 4)
my_car.describe_vehicle()
my_car.drive(100)
my_car.describe_vehicle()
