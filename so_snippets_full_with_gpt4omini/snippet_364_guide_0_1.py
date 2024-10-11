from time import sleep # pragma: no cover
from time import time # pragma: no cover

time_not_passed = True # pragma: no cover
init_time = time() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/377454/how-do-i-get-my-program-to-sleep-for-50-milliseconds
from l3.Runtime import _l_
try:
    import time
    _l_(3452)

except ImportError:
    pass
print("0.00 seconds")
_l_(3453)
time.sleep(0.05) # 50 milliseconds... make sure you put time. if you import time!
_l_(3454) # 50 milliseconds... make sure you put time. if you import time!
print("0.05 seconds")
_l_(3455)
try:
    from time import sleep
    _l_(3457)

except ImportError:
    pass
print("0.00 sec")
_l_(3458)
sleep(0.05) # Don't put time. this time, as it will be confused. You did
_l_(3459) # Don't put time. this time, as it will be confused. You did
            # not import the whole module
print("0.05 sec")
_l_(3460)

time_not_passed = True
_l_(3461)
try:
    from time import time
    _l_(3463)

except ImportError:
    pass

init_time = time() # Or time.time() if whole module imported
_l_(3464) # Or time.time() if whole module imported
print("0.00 secs")
_l_(3465)
while True:
    _l_(3469)

    if init_time + 0.05 <= time() and time_not_passed:
        _l_(3468)

        print("0.05 secs")
        _l_(3466)
        time_not_passed = False
        _l_(3467)

