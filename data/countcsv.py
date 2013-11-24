import csv

with open('test.csv', 'r') as fp:
    reader = csv.reader(fp)
    count = 0
    for row in reader:
        count += 1

print count
    

