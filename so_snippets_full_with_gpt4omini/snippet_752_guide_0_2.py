from datetime import timedelta, tzinfo, datetime, timezone # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2331592/why-does-datetime-datetime-utcnow-not-contain-timezone-information
from l3.Runtime import _l_
try:
    from datetime import timedelta, tzinfo
    _l_(1472)

except ImportError:
    pass

ZERO = timedelta(0)
_l_(1473)

# A UTC class.

class UTC(tzinfo):
    _l_(1480)

    """UTC"""

    def utcoffset(self, dt):
        _l_(1475)

        aux = ZERO
        _l_(1474)
        return aux

    def tzname(self, dt):
        _l_(1477)

        aux = "UTC"
        _l_(1476)
        return aux

    def dst(self, dt):
        _l_(1479)

        aux = ZERO
        _l_(1478)
        return aux

utc = UTC()
_l_(1481)
try:
    from datetime import datetime
    _l_(1483)

except ImportError:
    pass

now = datetime.now(utc)
_l_(1484)
try:
    from datetime import datetime, timezone
    _l_(1486)

except ImportError:
    pass

now = datetime.now(timezone.utc)
_l_(1487)

