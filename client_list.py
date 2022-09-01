def main():

    infile = open('clients.txt', 'r')

    number = 0

    for line in infile:

        number += 1

        print (number, '. ', line.rstrip('\n'), sep = '') 

main()