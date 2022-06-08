
class Person:
    species="Homo sapiens"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is  {self.age} years old"



p1 = Person('Precieux',17)

p1.species = 'Another Homo sapiens'
print(p1.description())