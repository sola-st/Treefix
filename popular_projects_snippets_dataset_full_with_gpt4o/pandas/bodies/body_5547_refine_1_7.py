import numpy as np # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pytest # pragma: no cover

NpyDatetimeUnit = type('Mock', (object,), {'NPY_FR_s': type('Mock', (object,), {'value': 's'})}) # pragma: no cover

import numpy as np # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pytest # pragma: no cover

class NpyDatetimeUnit:# pragma: no cover
    NPY_FR_s = type('Mock', (object,), {'value': 's'}) # pragma: no cover
class OutOfBoundsDatetime(Exception):# pragma: no cover
    pass # pragma: no cover
Timestamp._creso = 's' # pragma: no cover

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
