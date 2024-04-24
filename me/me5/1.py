"""
Write a menu driven python program to overload unary ‘+’, binary ‘+’, less than ’<‘,
greater than ’>’ operator on complex numbers.

"""
class Complx:
    def __init__(self, r=None, i=None):
        if not ( r or i ):
            data = input('Enter complex number : ')
            (r,i) = data.split('+') if '+' in data else (data, '0i')
            self.real, self.imag = int(r), int(i[:-1])
        else:
            self.real, self.imag = r,i
    def __add__(self,other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complx(r,i)
    def __pos__(self):
        return self
    def __lt__(self,other):
        mag1 = (self.real ** 2 + self.imag ** 2) ** 0.5# type: ignore
        mag2 = (other.real ** 2 + other.imag ** 2) ** 0.5
        return mag1 < mag2
    def __gt__(self,other):
        mag1 = (self.real ** 2 + self.imag ** 2) ** 0.5 # type: ignore
        mag2 = (other.real ** 2 + other.imag ** 2) ** 0.5
        return mag1 > mag2
    def __str__(self):
        return f'{self.real}+{self.imag}i' if self.imag > 0 else f'{self.real}' # type: ignore
print('Enter your choice')
option = int(input('1.uninary + \n2.binary + \n3.less than\n4.greater than\nchoice : '))
if option not in range(1,5):
    print('ERRR')
else:
    if option == 1:
        o1 = Complx()
        answer = +o1
    elif option == 2:
        o1 = Complx()
        o2 = Complx()
        answer = o1 + o2
    elif option == 3:
        o1 = Complx()
        o2 = Complx()
        answer = o1 < o2
    elif option == 4:
        o1 = Complx()
        o2 = Complx()
        answer = o1 > o2
    print('Answer :',answer)