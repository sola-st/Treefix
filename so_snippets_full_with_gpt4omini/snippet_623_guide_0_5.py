import datetime # pragma: no cover
class nptime: # pragma: no cover
    def __init__(self, hours, minutes, seconds): # pragma: no cover
        self.time = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds) # pragma: no cover
    def __add__(self, other): # pragma: no cover
        return self.time + other # pragma: no cover
    def __repr__(self): # pragma: no cover
        total_seconds = int(self.time.total_seconds()) # pragma: no cover
        hours, remainder = divmod(total_seconds, 3600) # pragma: no cover
        minutes, seconds = divmod(remainder, 60) # pragma: no cover
        return f'{hours:02}:{minutes:02}:{seconds:02}' # pragma: no cover

nptime = type('MockNptime', (object,), {'nptime': nptime})() # pragma: no cover

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

