# Olivia Polus C01

import csv

def read_file(filename):
    f = open(filename, "r", newline= "")
    reader = csv.reader(f)

    next(header)
    total = 0
    count = 0

    for row in reader :
        print(row)
        total += float(row[1])
        count += 1

    print("Average height : ", total/count)
    f.close()

def add_data (filename):
    gender = input("Enter gender :")
    height = input("Enter height : ")
    weight = input("Enter weight : ")
    bmi = input("Enter BMI : ")

    f = open(filename, "a", newline= "")
    writer = csv.writer(f)
    writer.writerow( [gender,height,weight,bmi] )
    f.close()

    f2 = open(filename, "r", newline= "")
    reader = csv.reader(f2)
    for row in reader :
        print(row)
    f2.close()

file = C:\Users\User\Downloads\bmi.csv
read_file(file)
add_data(file)


