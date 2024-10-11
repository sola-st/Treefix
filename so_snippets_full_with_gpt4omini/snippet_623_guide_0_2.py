import datetime # pragma: no cover

class MockNPTIME:  # Mock implementation for nptime # pragma: no cover
    def __init__(self, hours, minutes, seconds): # pragma: no cover
        self.total_seconds = hours * 3600 + minutes * 60 + seconds # pragma: no cover
    def __add__(self, other): # pragma: no cover
        return self.total_seconds + (other.total_seconds if isinstance(other, datetime.timedelta) else other) # pragma: no cover
    @classmethod # pragma: no cover
    def nptime(cls, hours, minutes, seconds): # pragma: no cover
        return cls(hours, minutes, seconds) # pragma: no cover
nptime = MockNPTIME # pragma: no cover

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

