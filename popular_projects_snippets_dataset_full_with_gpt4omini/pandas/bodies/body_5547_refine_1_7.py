import numpy as np # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pytest # pragma: no cover
from pandas.errors import OutOfBoundsDatetime # pragma: no cover

import numpy as np # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pytest # pragma: no cover
from pandas.errors import OutOfBoundsDatetime # pragma: no cover

class NpyDatetimeUnit: pass # pragma: no cover
NpyDatetimeUnit.NPY_FR_s = type('Mock', (object,), {'value': 1})() # pragma: no cover
np.datetime64 = np.datetime64 # pragma: no cover
np.iinfo = np.iinfo # pragma: no cover
np.int64 = np.int64 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
from l3.Runtime import _l_
out_of_bounds_dates = ("1677-09-21", "2262-04-12")
_l_(7152)

time_units = ("D", "h", "m", "s", "ms", "us")
_l_(7153)

for date_string in out_of_bounds_dates:
    _l_(7160)

    for unit in time_units:
        _l_(7159)

        dt64 = np.datetime64(date_string, unit)
        _l_(7154)
        ts = Timestamp(dt64)
        _l_(7155)
        if unit in ["s", "ms", "us"]:
            _l_(7158)

            # We can preserve the input unit
            assert ts.value == dt64.view("i8")
            _l_(7156)
        else:
            # we chose the closest unit that we _do_ support
            assert ts._creso == NpyDatetimeUnit.NPY_FR_s.value
            _l_(7157)
info = np.iinfo(np.int64)
_l_(7161)
msg = "Out of bounds nanosecond timestamp:"
_l_(7162)
for value in [info.min + 1, info.max]:
    _l_(7167)

    for unit in ["D", "h", "m"]:
        _l_(7166)

        dt64 = np.datetime64(value, unit)
        _l_(7163)
        with pytest.raises(OutOfBoundsDatetime, match=msg):
            _l_(7165)

            Timestamp(dt64)
            _l_(7164)

in_bounds_dates = ("1677-09-23", "2262-04-11")
_l_(7168)

for date_string in in_bounds_dates:
    _l_(7172)

    for unit in time_units:
        _l_(7171)

        dt64 = np.datetime64(date_string, unit)
        _l_(7169)
        Timestamp(dt64)
        _l_(7170)
