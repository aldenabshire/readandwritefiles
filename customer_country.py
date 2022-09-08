import csv

infile = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

outfile.write('Full Name, Country' + '\n')

for record in csvfile:

    fname = record[1]
    lname = record[2]
    country = record[4]

    data = (fname + ' ' + lname  + ', ' + country)

    outfile.write(data + '\n')


infile.close()
outfile.close()


