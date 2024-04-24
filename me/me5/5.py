"""
Write a python code to perform the CRUD operations on amp table .Write output for
each CRUD operation.
"""
import csv
fields = ['roll','student','age']
def create_record(data):
    f = open('data.csv','w',newline='')
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writerows(data)
    f.close()
def read_record(data, roll):
    f = open('data.csv','r')
    reader = csv.DictReader(f,fieldnames=fields)
    for data in reader:
        if data['roll'] == str(roll):
            for (key,value) in data.items():
                print(f'{key} = {value}')
    f.close()
def update_record(data):
    f = open('data.csv','a',newline='')
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writerow(data)
    f.close()
def delete_record(data):
    records = []
    f = open('data.csv','a')