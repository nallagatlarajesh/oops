# inheritance allows ypu to create a new class (subclass or derived class ) based on an existing  class
#the new class inherits the attributes and methods of the base class and can also add its own

#code for 
# inheritence example

class animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        pass #placeholder methode ,you can give anything here
    
class Dog(animal):
    def speak(self):
        return f"{self.name} barks!" 
    
class Cat(animal):
    def speak(self):
        return f"{self.name} meows!"

#creating objects (instance) of animal or class
dog=Dog( " puppy")
cat=Cat("milky")

#accessing attributes
print("dog name is", dog.name)
print(dog.speak()) 
print(cat.name)
print(cat.speak())
