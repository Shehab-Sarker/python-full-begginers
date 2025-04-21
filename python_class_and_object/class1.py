# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


class Myclass:
    x=5
    
print(Myclass)
print("")

# Now we can use the class named MyClass to create objects:

p1=Myclass()
print(p1.x)
print("")

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# Example
# Create a class named Person, use the __init__() function to assign values for name and age:

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p2=person("Johm",36)

print(p2.name)
print(p2.age)

# The __init__() function is called automatically every time the class is being used to create a new object.
print("")

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

class  Person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name}({self.age})"
    
p3=Person1("shehab","23")
print(p3)
print()

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def myfunc(self):
        print(f"Hello my name is {self.name} and age is {self.age}")
        
p4=Person2("shehab",23)
p4.myfunc()        


        