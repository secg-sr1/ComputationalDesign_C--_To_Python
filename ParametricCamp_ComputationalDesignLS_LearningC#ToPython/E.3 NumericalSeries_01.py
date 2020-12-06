print("First ten numbers:")
for i in range(0,10):
    print(i)

###
    
print("First ten numbers:")
for i in range(0,-10,-1):
    print(i)

###

print("First ten square numbers")
for i in range(0,10):
    print(i*i)

###

print("First ten even numbers")
for i in range(0,20,2):
    print(i)

###
    
print("First ten even numbers:")
found = 0
for i in range(0,100):
    if i % 2 == 0:
        print(i)
        found += 1
        
        if found >= 10:
            break

###
        
print("First ten odd numbers:")
for i in range(1,20,2):
    print(i)

###

print("First ten odd numbers:")
for i in range(0,10):
    print(2*i+1)

###

found = 0
for i in range(0,100):
    if i % 2 == 1:
        print(i)
        found += 1
        if found >= 10:
            break

###

multValue = 23453
print('The multiplication table for number %s'%(multValue))
for i in range(0,10):
    print('multValue x i = %s '%(multValue * i))

###

print("An ascending geometric series:")
n = 10
a = 1
r = 1.50

prev_term = a
sum_gp = a
for i in range(n):
    ith_term = r * prev_term
    print("{}".format(ith_term))
    prev_term = ith_term
    #print(ith_term)
    sum_gp = sum_gp +ith_term
#print(sum_gp)


#Reference https://www.codespeedy.com/sum-of-geometric-progression-series-in-python/

###
alphabet = ""
alphabetLowCase = ""
for i in range(0,26):
    alphabet += chr(65+i)
    alphabetLowCase += chr(97+i)
    print(i,':{}'.format(alphabet))

###

print("The addition of the first ten numbers")
massAddition = 0;

for i in range(0,10):
    massAddition += i
print(massAddition)

###

print("Fibonacci sequence")
prev1 = 1
prev2 = 1
print(prev1)
print(prev2)

for i in range(0,10):
    sum = prev1 + prev2
    print(sum)
    
    prev1 = prev2
    prev2 = sum

###

print("Prime numbers")
for i in range(2,100):
    isPrime = True
    for j in range(2,i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime == True:
        print(i)
