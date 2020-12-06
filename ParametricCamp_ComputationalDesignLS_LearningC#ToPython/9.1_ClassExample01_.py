#Class Constructor 

class Person:
    #Fields
    name: str
    age: int
    height: float
    isAlive: bool
    
    #Constructor
    def __init__(self, name, age, height, isAlive):
        self.name = name
        self.age = age
        self.height = height
        self.isAlive = isAlive

p = Person("Jose Luis", 100, 5.9, True)
mj = Person("MaryJane", 33, 4.2, True)


print(p.name)
print(p.age)
print(p.height)
print(p.isAlive)

print(mj.name)
print(mj.age)
print(mj.height)
print(mj.isAlive)
