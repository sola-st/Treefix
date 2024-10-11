import datetime # pragma: no cover
import sys # pragma: no cover
import types # pragma: no cover

class MockNptime: # pragma: no cover
    def __init__(self, hour, minute, second): # pragma: no cover
        self.hour = hour # pragma: no cover
        self.minute = minute # pragma: no cover
        self.second = second # pragma: no cover
    def __add__(self, other): # pragma: no cover
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second + other.total_seconds() # pragma: no cover
        hours, remainder = divmod(total_seconds, 3600) # pragma: no cover
        minutes, seconds = divmod(remainder, 60) # pragma: no cover
        return MockNptime(hours % 24, minutes, seconds) # pragma: no cover
def nptime_func(hour, minute, second): # pragma: no cover
    return MockNptime(hour, minute, second) # pragma: no cover
nptime = types.ModuleType('nptime') # pragma: no cover
setattr(nptime, 'nptime', nptime_func) # pragma: no cover
sys.modules['nptime'] = nptime # pragma: no cover

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

