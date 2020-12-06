import datetime

x = datetime.datetime.now()
print(x)

class Person:
    #Fields
    name: str
    YOB: int
    height: float
    isAlive: bool
    
    #Constructor
    def __init__(self, name, YOB, height):
        self.name = name
        self.YOB = YOB
        self.height = height
        
        currentYear = int(x.strftime("%Y"))
    
        if self.YOB > currentYear:
            self.isAlive = True
        else:
            self.isAlive = False
    def __bool__(self):
        return self.isAlive
        


p = Person("Jose Luis", 2050, 5.9)
mj = Person("MaryJane", 2000, 4.2)

print(p.name)
print(p.YOB)
print(p.height)
print(p.isAlive)

print(mj.name)
print(mj.YOB)
print(mj.height)
print(mj.isAlive)
