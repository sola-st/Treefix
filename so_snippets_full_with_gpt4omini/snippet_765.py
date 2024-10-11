# Extracted from https://stackoverflow.com/questions/92928/time-sleep-sleeps-thread-or-process
import time
from threading import Thread

class worker(Thread):
    def run(self):
        for x in xrange(0,11):
            print x
            time.sleep(1)

class waiter(Thread):
    def run(self):
        for x in xrange(100,103):
            print x
            time.sleep(5)

def run():
    worker().start()
    waiter().start()

thread_test.run()
0
100
1
2
3
4
5
101
6
7
8
9
10
102

