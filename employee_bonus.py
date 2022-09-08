import csv

infile = open('EmployeePay.csv', 'r')

csvfile = csv.reader(infile, delimiter = ',')

for row in csvfile:

    print(row[0], row[1], row[2], row[3], row[4])

infile.close()
