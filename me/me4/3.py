"""
Define a class Person with attributes name and age, and a method display_info() to display the name and 
age of the person.
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print('Person Info:')
        print(f'name : {self.name}\nage : {self.age}')
name = input('your name : ')
age = input('your age : ')
obj = Person(name,age)
obj.display_info()