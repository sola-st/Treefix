# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(13839)

except ImportError:
    pass
try:
    from time import mktime
    _l_(13841)

except ImportError:
    pass

dt = datetime.now()
_l_(13842)
sec_since_epoch = mktime(dt.timetuple()) + dt.microsecond/1000000.0
_l_(13843)

millis_since_epoch = sec_since_epoch * 1000
_l_(13844)

