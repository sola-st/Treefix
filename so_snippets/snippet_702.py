# Extracted from https://stackoverflow.com/questions/85451/pythons-time-clock-vs-time-time-accuracy
import time

def t_time():
    start=time.time()
    time.sleep(0.1)
    return (time.time()-start)


def t_clock():
    start=time.clock()
    time.sleep(0.1)
    return (time.clock()-start)




counter_time=0
counter_clock=0

for i in range(1,100):
    counter_time += t_time()

    for i in range(1,100):
        counter_clock += t_clock()

print "time() =",counter_time/100
print "clock() =",counter_clock/100

time() = 0.0993799996376

clock() = 0.0993572257367

