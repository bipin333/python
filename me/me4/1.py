"""
Define a class Vehicle with attributes make and model, and a method display_info() that prints 
the make and model of the vehicle. Then, create two subclasses Car and Motorcycle that inherit from 
Vehicle and add an additional attribute year to both subclasses. Override the display_info() method in each
subclass to include the year of the vehicle.
"""
class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def display_info(self):
        print(f'Type : {self.make}, {self.model}')
class Car(Vehicle):
    def __init__(self,make,model,year):
        Vehicle.__init__(self,make,model)
        self.year = year
    def display_info(self):
        print('Car info :')
        Vehicle.display_info(self)
        print(f'Year : {self.year}')
class Motorcycle(Vehicle):
    def __init__(self,make,model,year):
        Vehicle.__init__(self,make,model)
        self.year = year
    def display_info(self):
        print('Motorcycle info :')
        Vehicle.display_info(self)
        print(f'Year : {self.year}')
choice = int(input('what do you want to input:\n1.Car\n2.Motorcycle\nchoice : '))
if choice not in range(1,3):
    print('ERR')
else:
    make_name = input('Enter make name : ')
    model_name = input('Enter model name : ')
    year = input('Enter Year : ')
    if choice==1:
        obj = Car(make_name,model_name,year)
    else:
        obj = Motorcycle(make_name,model_name,year)
    obj.display_info()