"""
Write a program to calculate the length of a string 
and convert the given lowercase into uppercase if length 
of string is greater or equal to 10 otherwise convert into 
lowercase.
"""
s = input('String : ')
if len(s) >= 10:
    s = s.upper()
else:
    s = s.lower()
print('Final String :',s)