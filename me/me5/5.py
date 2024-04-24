"""
Write a python code to perform the CRUD operations on amp table .Write output for
each CRUD operation.
"""
import csv
fields = ['roll','student','age']
def create_record(records):
    f = open('amp.csv','w',newline='')
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)
    f.close()
def read_record(roll):
    f = open('amp.csv','r')
    reader = csv.DictReader(f,fieldnames=fields)
    for data in reader:
        if data['roll'] == str(roll):
            for (key,value) in data.items():
                print(f'{key} = {value}')
    f.close()
def update_record(data):
    f = open('amp.csv','a',newline='')
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writerow(data)
    f.close()
def delete_record(roll):
    records = []
    f = open('amp.csv','r')
    reader = csv.DictReader(f,fieldnames=fields)
    for data in reader:
        if data['roll'] != str(roll):
            records.append(data)
    f.close()
    create_record(records)

option = int(input('Select option\n1.Create Records\n2.Read Record\n3.Update Record\n4.Delete Record\nchoice = '))
if option in range(1,5):
    if option == 1:
        num = int(input('How many records do you want : '))
        records = []
        for i in range(num):
            data = {}
            print('data',i+1)
            for j in fields:
                data[j] = input(f'Enter {j} :')
            records.append(data)
        create_record(records)
    elif option == 2:
        roll = input('Enter roll : ')
        read_record(roll)
    elif option == 3:
        data = {}
        for j in fields:
            data[j] = input(f'Enter {j} :')
        update_record(data)
    elif option==4:
        roll = input('Enter roll : ')
        delete_record(roll)
else:
    print('ERR')