#Lists a
numbers = []

numbers.append(0)
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)
numbers.append(60)
numbers.append(60)
numbers.append(60)
numbers.append(60)
numbers.append(60)

numbers[0] = 23

for i in range(0,len(numbers)):
    print(numbers[i])

#print(numbers[0])

#Lists b 
numbers = []
elements = 25

#Add elements
for i in range(0,elements):
    numbers.append(10*i)

#Manually override values on a list
#numbers[0] = 23
for i in range(0, len(numbers)):
    numbers[i]*=2

#Print all elements
for i in range(0, len(numbers)):
    print(numbers[i])

