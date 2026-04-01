def read_bmi_file(parameter):
    f= open (filename, "r", newline = "")
    reader = csv.reader(f)

    next(reader)
    total = 0
    count = 0

    for row in reader : 
        print(row)
        total += float(row[1])
        count += 1

    print("Average Height : " total/count)
    f.close()

def add_data(filename):
    gender = input("Enter Gender :")
    height
    weight
    bmi 

    f= open(filename, "a", newline = "")
    writer = csv.writer(f)
    writer.writerow([gender, height, weight, bmi])
    f.close()

    f2 = open(filename, "r", newline= "")
    reader = csv.reader(f2)
    for row in reader :
        print(row)
    f2.close()

