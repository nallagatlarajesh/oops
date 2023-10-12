class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def introduce(self):
        return f" iam {self.name} my age is {self.age}"
    
#creating an object or instance of class
person1=person("rajesh",25)

#accessing attributes of the person class
print(person1.name)
print(person1.introduce())
