# <!-- Looping Array Elements -->
# <!-- We can use the for in loop to loop through all the elements of an array. -->
cars=["Ford", "Volvo","BMM"]

for x in cars:
    print(x,end=" ")
 
 
# Adding Array Elements
# YWe can use the append() method to add an element to an array.  

print("")

cars.append("Honda")

for x in cars:
    print(x, end=" ")
    
# Removing Array Elements
# We can use the pop() method to remove an element from the array.
cars.pop(2)
print("")
print(cars)
print(" ")

# We can also use the remove() method to remove an element from the array.
cars.remove("Honda")
print(cars)