"""
WAP to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly'. 
If the string length of the given string is less than 3, 
leave it unchanged.
"""
string = input('String : ')
if len(string) < 3:
    pass
elif string[len(string)-3:] == 'ing':
    string += 'ly'
else:
    string += 'ing'
print('Final String :',string)