
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def bark(self):
        print(f"{self.name} barks!")

#creating objects (instances ) of the dog class
dog1=dog("buddy ",3)
dog2=dog("rex",5)

#accessing attributes and calling methodes
print(dog1.name)    
dog2.bark()
