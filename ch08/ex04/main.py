import csv

with open('books.csv', 'rt') as fin:
    books = csv.DictReader(fin)

    print([row for row in books])
