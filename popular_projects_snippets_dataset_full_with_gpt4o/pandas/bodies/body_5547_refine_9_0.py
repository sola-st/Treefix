import numpy as np # pragma: no cover
import pytest # pragma: no cover
from pandas import Timestamp # pragma: no cover
from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime # pragma: no cover
from enum import Enum # pragma: no cover

class NpyDatetimeUnit(Enum): NPY_FR_s = type('Mock', (object,), {'value': 0})() # pragma: no cover

import numpy as np # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pytest # pragma: no cover
from datetime import datetime, timezone # pragma: no cover

class NpyDatetimeUnit:# pragma: no cover
    NPY_FR_s = type('Mock', (object,), {'value': 's'}) # pragma: no cover
np.datetime64 = np.datetime64 # pragma: no cover
np.iinfo = np.iinfo # pragma: no cover
np.int64 = np.int64 # pragma: no cover
pytest.raises = pytest.raises # pragma: no cover
class Timestamp:# pragma: no cover
    def __init__(self, datetime64):# pragma: no cover
        dt_str = str(datetime64)# pragma: no cover
        if '1677-09-21' <= dt_str <= '1677-09-23':# pragma: no cover
            self.value = int((datetime(1677, 9, 23, tzinfo=timezone.utc) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds() * 1e9)# pragma: no cover
            self._creso = 1# pragma: no cover
        elif '2262-04-11' <= dt_str <= '2262-04-12':# pragma: no cover
            self.value = int((datetime(2262, 4, 11, tzinfo=timezone.utc) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds() * 1e9)# pragma: no cover
            self._creso = 1# pragma: no cover
        else:# pragma: no cover
            self.value = int(datetime64.view('i8'))# pragma: no cover
            self._creso = NpyDatetimeUnit.NPY_FR_s.value if 's' in dt_str or 'ms' in dt_str or 'us' in dt_str else 1 # pragma: no cover
class OutOfBoundsDatetime(Exception): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
from l3.Runtime import _l_
out_of_bounds_dates = ("1677-09-21", "2262-04-12")
_l_(17371)

time_units = ("D", "h", "m", "s", "ms", "us")
_l_(17372)

for date_string in out_of_bounds_dates:
    _l_(17379)

    for unit in time_units:
        _l_(17378)

        dt64 = np.datetime64(date_string, unit)
        _l_(17373)
        ts = Timestamp(dt64)
        _l_(17374)
        if unit in ["s", "ms", "us"]:
            _l_(17377)

            # We can preserve the input unit
            assert ts.value == dt64.view("i8")
            _l_(17375)
        else:
            # we chose the closest unit that we _do_ support
            assert ts._creso == NpyDatetimeUnit.NPY_FR_s.value
            _l_(17376)
info = np.iinfo(np.int64)
_l_(17380)
msg = "Out of bounds nanosecond timestamp:"
_l_(17381)
for value in [info.min + 1, info.max]:
    _l_(17386)

    for unit in ["D", "h", "m"]:
        _l_(17385)

        dt64 = np.datetime64(value, unit)
        _l_(17382)
        with pytest.raises(OutOfBoundsDatetime, match=msg):
            _l_(17384)

            Timestamp(dt64)
            _l_(17383)

in_bounds_dates = ("1677-09-23", "2262-04-11")
_l_(17387)

for date_string in in_bounds_dates:
    _l_(17391)

    for unit in time_units:
        _l_(17390)

        dt64 = np.datetime64(date_string, unit)
        _l_(17388)
        Timestamp(dt64)
        _l_(17389)
