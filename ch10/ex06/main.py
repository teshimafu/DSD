import multiprocessing
import random


def process(id, sleeptime):
    import time
    import os
    print('this is ', id, ' process in', os.getpid())
    print("I sleep", sleeptime)
    time.sleep(sleeptime)
    print("I wake up !")


if __name__ == '__main__':
    for i in range(0, 5):
        waittime = random.random()*5
        p = multiprocessing.Process(target=process, args=(i, waittime))
        p.start()
