# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
from l3.Runtime import _l_
try:
    import time
    _l_(484)

except ImportError:
    pass
start_time = time.perf_counter ()
_l_(485)
for x in range(1, 100):
    _l_(487)

    print(x)
    _l_(486)
end_time = time.perf_counter ()
_l_(488)
print(end_time - start_time, "seconds")
_l_(489)

