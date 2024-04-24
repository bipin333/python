"""
Write a python program to perform function overloading with different ways .
"""
#with default paramater
def area(l,b=None):
    if not b:
        return l*l
    else:
        return l*b
# with *args
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
#using different functions
def volume_cube(l):
    return l ** 3
def volume_cuboid(l,b,h):
    return l*b*h

print('area of square(5) :',area(5))
print('area of rectangle(5,2) :',area(5,2))
print('sum of 1,2 : ',add(1,2))
print('sum of 1,2,5,22 :',add(1,2,5,22))
print('volume of cube(5) :',volume_cube(5))
print('volume of cuboid(5,10,3) :',volume_cuboid(5,10,3))