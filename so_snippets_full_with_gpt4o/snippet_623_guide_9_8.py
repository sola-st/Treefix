import datetime # pragma: no cover
import sys # pragma: no cover
from types import ModuleType # pragma: no cover

class MockNptime: # pragma: no cover
    def __init__(self, h, m, s): # pragma: no cover
        self.h = h # pragma: no cover
        self.m = m # pragma: no cover
        self.s = s # pragma: no cover
    def __add__(self, timedelta): # pragma: no cover
        total_seconds = (self.h * 3600 + self.m * 60 + self.s + int(timedelta.total_seconds())) % 86400 # pragma: no cover
        h, rem = divmod(total_seconds, 3600) # pragma: no cover
        m, s = divmod(rem, 60) # pragma: no cover
        return MockNptime(h, m, s) # pragma: no cover
mocked_nptime = ModuleType('nptime') # pragma: no cover
mocked_nptime.nptime = MockNptime # pragma: no cover
sys.modules['nptime'] = mocked_nptime # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python
from l3.Runtime import _l_
try:
    import datetime
    _l_(15088)

except ImportError:
    pass
try:
    import nptime
    _l_(15090)

except ImportError:
    pass
nptime.nptime(11, 34, 59) + datetime.timedelta(0, 3)
_l_(15091)
nptime(11, 35, 2)
_l_(15092)

