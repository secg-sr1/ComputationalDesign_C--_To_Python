#Some values i want to compare 
value = 2
min = 0
max = 5

if value > max or value < min:
    print('%s is outside the [%s, %s] interval'%(value,min, max))

elif value > min and value < max:
    print('%s is inside the [%s, %s] interval'%(value, min, max))
