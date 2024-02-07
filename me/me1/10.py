"""
Write a program to accept sales from the user and calculate commission accordingly,
>=90 A Grade
>=80 and <=89 B Grade
>=70 and <=79 C Grade
<70 D Grade
"""
sales = int(input('Sales : '))
if sales >= 90:
    print('Commission : A Grade')
elif sales >= 80:
    print('Commission : B Grade')
elif sales >= 70:
    print('Commission : C Grade')
else:
    print('Commission : D Grade')