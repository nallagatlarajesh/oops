from  abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2
class square(shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        return self.side**2
    
#create an object of derived classes  
#function calling here
circle1=circle(5)
square1=square(4)

#accessing attributes 
print(circle1.area())
print(square1.area())
