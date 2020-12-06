import math

while True:
    try:
        print("Enter first value:")
        val1str = float(input())
        print("Enter second value:")
        val2str = float(input())
        break
    except:
        print("Enter numerical value")
val1 = val1str
val2 = val2str

print(type(val1))
print(type(val2))

print("HERE ARE SOME CALCULATIONS:")

#Displaying a bunch of computation with these values
add = val1 + val2
print(val1, "+" , val2, "=" , add)

sub = val1 - val2
print(val1, "-" , val2, "=" , sub)

mult = val1 * val2
print(val1, "*" , val2, "=" , mult)

div = val1 / val2
print(val1, "/" , val2, "=" , div)

mod = val1 % val2
print(val1, "%" , val2, "=" , mod)

sqrt = math.sqrt(val1)
print("Square root of",val1, "=" , sqrt)
