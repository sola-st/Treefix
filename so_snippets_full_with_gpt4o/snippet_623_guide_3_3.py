import datetime # pragma: no cover

class MockNptime: # pragma: no cover
    def __init__(self, hours, minutes, seconds): # pragma: no cover
        self.hours = hours # pragma: no cover
        self.minutes = minutes # pragma: no cover
        self.seconds = seconds # pragma: no cover
    def __add__(self, other): # pragma: no cover
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + other.total_seconds() # pragma: no cover
        hours, remainder = divmod(total_seconds, 3600) # pragma: no cover
        minutes, seconds = divmod(remainder, 60) # pragma: no cover
        return MockNptime(hours % 24, minutes, seconds) # pragma: no cover
def nptime(hours, minutes, seconds): # pragma: no cover
    return MockNptime(hours, minutes, seconds) # pragma: no cover

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

