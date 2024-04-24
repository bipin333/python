"""
C o n s i d e r a f i l e “ e m p . c s v ” w h i c h c o n t a i n s t h e f o l l o w i n g
information:empno,ename,sal.Write a python program to analyse this file and print
ename and salary of all employees who earn a salary greater than Rs. 20000.Also store
this information into a file “sal.csv”.
"""
import csv
file_in = open("emp.csv")
reader = csv.DictReader(file_in)
fields = reader.fieldnames
file_out = open("sal.csv",'w',newline='')
writer = csv.DictWriter(file_out,fieldnames=fields) # type: ignore
print('-----------')
for data in reader:
    if int(data['sal']) > 20000:
        writer.writerow(data)
        for (key,value) in data.items():
            print(f'{key} = {value}')
        print('-----------')