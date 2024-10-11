import pytest # pragma: no cover
import pytz # pragma: no cover
from pandas import Timestamp # pragma: no cover

class MockTimezones:  # pragma: no cover
    def maybe_get_tz(self, x): # pragma: no cover
        if isinstance(x, float): # pragma: no cover
            raise TypeError('<class \'float\'>') # pragma: no cover
        elif isinstance(x, type(pytz)): # pragma: no cover
            raise TypeError('<class \'module\'>') # pragma: no cover
        elif isinstance(x, Timestamp): # pragma: no cover
            raise TypeError('<class \'pandas._libs.tslibs.timestamps.Timestamp\'>') # pragma: no cover
timezones = MockTimezones() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
from l3.Runtime import _l_
with pytest.raises(TypeError, match="<class 'float'>"):
    _l_(10456)

    timezones.maybe_get_tz(44.0)
    _l_(10455)

with pytest.raises(TypeError, match="<class 'module'>"):
    _l_(10458)

    timezones.maybe_get_tz(pytz)
    _l_(10457)

msg = "<class 'pandas._libs.tslibs.timestamps.Timestamp'>"
_l_(10459)
with pytest.raises(TypeError, match=msg):
    _l_(10461)

    timezones.maybe_get_tz(Timestamp("2021-01-01", tz="UTC"))
    _l_(10460)
