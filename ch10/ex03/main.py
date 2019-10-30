import time
with open('today.txt', 'rt') as fin:
    today_string = fin.read()
    print(today_string)
    print(time.strptime(today_string, '%Y-%m-%d\n'))
