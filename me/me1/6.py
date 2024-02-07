"""
Python Program to Find Largest of 3 Numbers (Greatest of Three Numbers in Python)
"""
num1 = int(input('num1 : '))
num2 = int(input('num2 : '))
num3 = int(input('num3 : '))
if num1 > num2 and num1 > num3:
    print(num1,'is greatest')
elif num2 > num1 and num2 > num3:
    print(num2,'is greatest')
else:
    print(num3,'is greatest')