#code for 
# inheritence example and polymorphism


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

#polymorphism example

def animal_speak(animal):   #meth0de  only one methode , speak
    print(animal.speak())
animal_speak(dog)            #dog class 
animal_speak(cat)            #cat class
