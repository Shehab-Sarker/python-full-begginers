# Dictionary
# For dictionaries len() returns the number of key/value pairs in the dictionary:

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

print("Dictionary Length:",len(thisdict))
print()

# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def move(self):
        print("Drive")
        
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def move(self):
        print("Sail")
        
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def move(self):
        print("Fly")
        
        
car1=Car("Ford","Mustang")
boat1=Boat("Ibizia","Touring 20")
plane1=Plane("Boieng","747")

for x in (car1,boat1,plane1):
    x.move()