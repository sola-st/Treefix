import datetime # pragma: no cover
import sys # pragma: no cover
from types import ModuleType # pragma: no cover

class MockNptime: # pragma: no cover
    def __init__(self, hour, minute, second): # pragma: no cover
        self.time = datetime.time(hour, minute, second) # pragma: no cover
    def __add__(self, other): # pragma: no cover
        combined_datetime = datetime.datetime.combine(datetime.date.today(), self.time) + other # pragma: no cover
        new_time = combined_datetime.time() # pragma: no cover
        return MockNptime(new_time.hour, new_time.minute, new_time.second) # pragma: no cover
mock_nptime_module = ModuleType('nptime') # pragma: no cover
mock_nptime_module.nptime = MockNptime # pragma: no cover
sys.modules['nptime'] = mock_nptime_module # pragma: no cover

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

