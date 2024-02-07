"""
Write a program to make simple calculator.
"""
num1 = float(input('num1 : '))
num2 = float(input('num2 : '))
choice = int(input('Choose One Operation:\n1.ADD\n2.SUB\n3.MUL\n4.DIV\nchoice : '))
if choice == 1:
    print('Answer :',num1+num2)
elif choice == 2:
    print('Answer :',num1-num2)
elif choice == 3:
    print('Answer :',num1*num2)
elif choice == 4:
    if num2 == 0:
        print('ERROR DIVISION BY 0')
    else:
        print('Answer :',num1/num2)
else:
    print('ERROR')