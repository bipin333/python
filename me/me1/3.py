"""
Write a program to find larger between two strings.
"""
s1 = input('string : ')
s2 = input('string : ')
if len(s1) > len(s2):
    print('string',s1,'is larger')
elif len(s2) > len(s1):
    print('string',s2,'is larger')
else:
    print('Both string are equally large')