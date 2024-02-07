"""
Write a program to swap two floating point numbers and 
convert the first number to int and find the round off 
value of second number
"""
num1 = float(input('num1 : '))
num2 = float(input('num2 : '))
tmp = num1
num1 = num2
num2 = tmp
print('final num1 :',int(num1))
print('final num2 :',round(num2))