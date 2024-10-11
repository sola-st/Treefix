def func1(): time.sleep(0.1) # pragma: no cover
def func2(): time.sleep(0.2) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
from l3.Runtime import _l_
try:
    import timeit
    _l_(2978)

except ImportError:
    pass

start_time = timeit.default_timer()
_l_(2979)
func1()
_l_(2980)
print(timeit.default_timer() - start_time)
_l_(2981)

start_time = timeit.default_timer()
_l_(2982)
func2()
_l_(2983)
print(timeit.default_timer() - start_time)
_l_(2984)

