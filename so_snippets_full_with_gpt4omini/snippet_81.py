# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python
from l3.Runtime import _l_
try:
    import time
    _l_(2103)

except ImportError:
    pass

start = time.time()
_l_(2104)
print("hello")
_l_(2105)
end = time.time()
_l_(2106)
print(end - start)
_l_(2107)

