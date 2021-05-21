def compare(a, b, *difference, **msg):

    if a > b:
        msg = str(a) +" Is greater than " + str(b)
        print(msg)
    elif a < b:
        msg = str(a) + " Is smaller than " + str(b)
        print(msg)
    else:
        msg = str(a) + " Is equal to " + str(b)
        print(msg)
    

    difference = a - b
    print(difference)
    return a > b


a = 5
b = 3
print(compare(a, b))


        

