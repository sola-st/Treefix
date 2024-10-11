# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
from l3.Runtime import _l_
try:
    import time
    _l_(12425)

except ImportError:
    pass
start_time = time.perf_counter ()
_l_(12426)
for x in range(1, 100):
    _l_(12428)

    print(x)
    _l_(12427)
end_time = time.perf_counter ()
_l_(12429)
print(end_time - start_time, "seconds")
_l_(12430)

