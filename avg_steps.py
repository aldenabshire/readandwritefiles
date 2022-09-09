import csv
import calendar

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

month = 1
total = 0
num = 0
a = 1

outfile.write('Month, Steps' + '\n')


for row in csvfile:

    if int(row[0]) == month:

        num += 1
        total += int(row[1])

        if int(row[0]) == 12:

            month_name = calendar.month_name[a]            
            average = round(total/num, 2)
            answer = str(average)

            outfile.write(month_name + ', ' + answer + '\n')

            break

    else:

        average = round(total/num, 2)
        answer = str(average)
        month_name = calendar.month_name[a]

        outfile.write(month_name + ', ' + answer + '\n')

        a += 1
        num = 1
        total = int(row[1])
        month = int(row[0])

outfile.close()