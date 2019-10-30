from datetime import date
today_string=''
with open('today.txt', 'rt') as fin:
    today_string = fin.readline()
    print(today_string)
