# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
        
#Use the Person class to create an object, and then execute the printname method:

x=Person("Shehab","Sarker")
x.printname()

# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass

y=Student("Mahi","Abdullah")
y.printname()
print()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.The child's __init__() function overrides the inheritance of the parent's __init__() function

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student1(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # Person.__init__(self,fname, lname)
        
y1=Student1("Rifat","Sarker")
y1.printname()
print()

# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

class Student3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduaton_year=2027

y3=Student3("Bangla","Desh")
y3.printname()
print(y3.graduaton_year)
print()

# Add a method called welcome to the Student class:
class Student4(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.year=year
        
    def welcome(self):
        print("Welcome",self.fname,self.lname,self.year)
        
y4=Student4("Shehab","Sarker",2027)
y4.printname()
y4.welcome()
print(y4.year)