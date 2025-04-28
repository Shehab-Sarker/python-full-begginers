# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?
# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
# Example
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def move(self):
        print("Move!")


class Car(Vehicle):
    pass
        
class Boat(Vehicle):   
    def move(self):
        print("Sail")
        
class Plane(Vehicle):
        
    def move(self):
        print("Fly!")

car1=Car("Ford","Mustang")
boat1=Boat("Ibizia","Touring 20")
plane1=Plane("Boieng","747")

for x in (car1,boat1,plane1):
    x.move()
    
    
print()

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
    print()