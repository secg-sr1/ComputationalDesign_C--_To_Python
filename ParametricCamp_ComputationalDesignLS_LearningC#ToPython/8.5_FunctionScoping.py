#FuntionScope 

import math

TAU = 2 * math.pi

def CircleLength(radius):
    len = TAU * radius
    return len

r = 1
circleLen = CircleLength(r)
print(circleLen)
