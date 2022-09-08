import csv

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month = 1
total = 0
num = 0
a = 0


for row in csvfile:

    if int(row[0]) == month:

        num += 1
        total += int(row[1])

    else:

        average = round(total/num, 2)
        answer = str(average)


        outfile.write(months[a] + ', ' + answer + '\n')

        num = 0
        total = 0
        month += 1
        a += 1

outfile.close()
infile.close()
