
text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''

with open('books.csv', 'wt') as fout:
    fout.write(text)
