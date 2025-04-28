# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:


class Mynumbers:
    def __init__(self,n):
        self.n=n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n>=0:
            x=self.n
            self.n-=1
            return x
        else:
            raise StopIteration
    
myclass=Mynumbers(10)
myiter = iter(myclass)

for x in myiter:
    print(x)
    