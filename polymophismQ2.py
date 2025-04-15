# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses with different move behaviors
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"


# Function that uses polymorphism
def travel(vehicle: Vehicle):
    print(vehicle.move())

# Instantiate objects
my_car = Car()
my_plane = Plane()


# Use the same function for different vehicle types
travel(my_car)
travel(my_plane)

