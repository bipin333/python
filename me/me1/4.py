"""
The Fizzbuzz program prints the number from 1 to n with the following modifications.
    • For numbers divisible by 3, it prints "Fizz" instead of the number.
    • For numbers divisible by 5, it prints "Buzz" instead of the number.
    • For numbers divisible by both 3 and 5, it prints "FizzBuzz" instead of the number.
"""
n = int(input('value of n : '))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)