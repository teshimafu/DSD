from datetime import date
with open('today.txt', 'wt') as fout:
    print(date.today(), file=fout)
