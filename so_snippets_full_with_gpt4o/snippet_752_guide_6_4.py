import sys # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2331592/why-does-datetime-datetime-utcnow-not-contain-timezone-information
from l3.Runtime import _l_
try:
    from datetime import timedelta, tzinfo
    _l_(13246)

except ImportError:
    pass

ZERO = timedelta(0)
_l_(13247)

# A UTC class.

class UTC(tzinfo):
    _l_(13254)

    """UTC"""

    def utcoffset(self, dt):
        _l_(13249)

        aux = ZERO
        _l_(13248)
        return aux

    def tzname(self, dt):
        _l_(13251)

        aux = "UTC"
        _l_(13250)
        return aux

    def dst(self, dt):
        _l_(13253)

        aux = ZERO
        _l_(13252)
        return aux

utc = UTC()
_l_(13255)
try:
    from datetime import datetime
    _l_(13257)

except ImportError:
    pass

now = datetime.now(utc)
_l_(13258)
try:
    from datetime import datetime, timezone
    _l_(13260)

except ImportError:
    pass

now = datetime.now(timezone.utc)
_l_(13261)

