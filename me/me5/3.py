"""
Given the student dataset “stu.csv” which contains the following information roll
number, student name, city and marks(Maximum marks is 500). Assume that this
dataset can have null values in it. Write a python code using the csv module which reads
from this dataset and displays the student details for all students whose name starts with
the letter “S”, are from “Delhi” and secured more than 75% marks. Store this info into a
file “result.csv”. Show output for your code. Use proper exception handling mechanism
wherever applicable.
"""
import csv
file_in = open('stu.csv',mode='r')
reader = csv.DictReader(file_in)
field_names = reader.fieldnames
file_out = open('result.csv',mode='w',newline='') #without newline will empty spaces result.csv
writer = csv.DictWriter(file_out,fieldnames=field_names) # type: ignore
writer.writeheader()
print('-----------')
for data in reader:
    requirement = data['student name'][:1] == 'S' and data['city'] == 'Delhi' and int(data['marks']) > (0.75 * 500)
    if requirement:
        writer.writerow(data)
        for (key,value) in data.items():
            print(f'{key} = {value}')
        print('-----------')
file_in.close()
file_out.close()