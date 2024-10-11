import pytest # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pytz # pragma: no cover

timezones = type('Mock', (object,), {'maybe_get_tz': lambda x: None}) # pragma: no cover

import pytest # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pytz # pragma: no cover

class MockTimezones: # pragma: no cover
    def maybe_get_tz(self, x): # pragma: no cover
        if isinstance(x, (float, type(pytz), Timestamp)): # pragma: no cover
            raise TypeError(f"<class '{type(x).__name__}'>") # pragma: no cover
timezones = MockTimezones() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
from l3.Runtime import _l_
with pytest.raises(TypeError, match="<class 'float'>"):
    _l_(21493)

    timezones.maybe_get_tz(44.0)
    _l_(21492)

with pytest.raises(TypeError, match="<class 'module'>"):
    _l_(21495)

    timezones.maybe_get_tz(pytz)
    _l_(21494)

msg = "<class 'pandas._libs.tslibs.timestamps.Timestamp'>"
_l_(21496)
with pytest.raises(TypeError, match=msg):
    _l_(21498)

    timezones.maybe_get_tz(Timestamp("2021-01-01", tz="UTC"))
    _l_(21497)
