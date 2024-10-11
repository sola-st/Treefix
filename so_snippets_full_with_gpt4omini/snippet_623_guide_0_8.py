import datetime # pragma: no cover
import numpy as np # pragma: no cover

class nptime: # Mock for nptime# pragma: no cover
    def __init__(self, *args): pass# pragma: no cover
    @staticmethod# pragma: no cover
    def nptime(*args): return np.datetime64(datetime.time(*args)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python
from l3.Runtime import _l_
try:
    import datetime
    _l_(2564)

except ImportError:
    pass
try:
    import nptime
    _l_(2566)

except ImportError:
    pass
nptime.nptime(11, 34, 59) + datetime.timedelta(0, 3)
_l_(2567)
nptime(11, 35, 2)
_l_(2568)

