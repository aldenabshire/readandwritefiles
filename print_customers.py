import csv

infile = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

for record in csvfile:

    outfile.write(record[1])

    input()

infile.close()
outfile.close()

    

