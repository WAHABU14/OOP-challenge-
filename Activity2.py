class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for vehicle in vehicles:
    vehicle.move()
