# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/377454/how-do-i-get-my-program-to-sleep-for-50-milliseconds
from l3.Runtime import _l_
try:
    import time
    _l_(14388)

except ImportError:
    pass
print("0.00 seconds")
_l_(14389)
time.sleep(0.05) # 50 milliseconds... make sure you put time. if you import time!
_l_(14390) # 50 milliseconds... make sure you put time. if you import time!
print("0.05 seconds")
_l_(14391)
try:
    from time import sleep
    _l_(14393)

except ImportError:
    pass
print("0.00 sec")
_l_(14394)
sleep(0.05) # Don't put time. this time, as it will be confused. You did
_l_(14395) # Don't put time. this time, as it will be confused. You did
            # not import the whole module
print("0.05 sec")
_l_(14396)

time_not_passed = True
_l_(14397)
try:
    from time import time
    _l_(14399)

except ImportError:
    pass

init_time = time() # Or time.time() if whole module imported
_l_(14400) # Or time.time() if whole module imported
print("0.00 secs")
_l_(14401)
while True:
    _l_(14405)

    if init_time + 0.05 <= time() and time_not_passed:
        _l_(14404)

        print("0.05 secs")
        _l_(14402)
        time_not_passed = False
        _l_(14403)

