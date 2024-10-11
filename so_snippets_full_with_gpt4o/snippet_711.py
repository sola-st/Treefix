# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
from l3.Runtime import _l_
try:
    import timeit
    _l_(14675)

except ImportError:
    pass

start_time = timeit.default_timer()
_l_(14676)
func1()
_l_(14677)
print(timeit.default_timer() - start_time)
_l_(14678)

start_time = timeit.default_timer()
_l_(14679)
func2()
_l_(14680)
print(timeit.default_timer() - start_time)
_l_(14681)

