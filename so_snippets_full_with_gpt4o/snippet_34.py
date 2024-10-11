# Extracted from https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay
import time
from itertools import count

def buzzergen(period):
    nexttime = time.time() + period
    for i in count():
        now = time.time()
        tosleep = nexttime - now
        if tosleep > 0:
            time.sleep(tosleep)
            nexttime += period
        else:
            nexttime = now + period
        yield i, nexttime

from sleepy import buzzergen
import time
buzzer = buzzergen(3) # Planning to wake up each 3 seconds
print time.time()
buzzer.next()
print time.time()
time.sleep(2)
buzzer.next()
print time.time()
time.sleep(5) # Sleeping a bit longer than usually
buzzer.next()
print time.time()
buzzer.next()
print time.time()

1400102636.46
1400102639.46
1400102642.46
1400102647.47
1400102650.47

import random
for ring in buzzergen(3):
    print "now", time.time()
    print "ring", ring
    time.sleep(random.choice([0, 2, 4, 6]))

now 1400102751.46
ring (0, 1400102754.461676)
now 1400102754.46
ring (1, 1400102757.461676)
now 1400102757.46
ring (2, 1400102760.461676)
now 1400102760.46
ring (3, 1400102763.461676)
now 1400102766.47
ring (4, 1400102769.47115)
now 1400102769.47
ring (5, 1400102772.47115)
now 1400102772.47
ring (6, 1400102775.47115)
now 1400102775.47
ring (7, 1400102778.47115)

