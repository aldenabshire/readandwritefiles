import csv

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

stepsj = 0

for row in csvfile:

    if row[0] == 1:
        stepsj += row[1]

print('January', stepsj)
