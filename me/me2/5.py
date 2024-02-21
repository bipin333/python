"""
Python program to count number of vowels using sets in given string
"""
string = input('Enter a string : ')
string = set(string)
vowels = 'aeiouAEIOU'
vowel_count = 0
for i in string:
    if i in vowels:
        vowel_count += 1
print('Total Vowel :',vowel_count)