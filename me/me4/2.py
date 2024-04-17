"""
Define a class Shape with a method area() to calculate the area of the shape. Create subclasses 
Rectangle and Circle that inherit from Shape. Override the area() method in each subclass to calculate 
the area of a rectangle and a circle, respectively.
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2
choice = int(input('what do you want :\n1.Rectangle\n2.Circle\nchoice : '))
if choice not in range(1,3):
    print('ERR')
else:
    if choice == 1:
        len = float(input('length : '))
        bred = float(input('breadth : '))
        obj = Rectangle(len,bred)
        print(f'Area of Rectangle : {obj.area()}')
    else:
        radii = float(input('radius : '))
        obj = Circle(radii)
        print(f'Area of Circle : {obj.area()}')