import numpy as np # pragma: no cover

iNaT = np.datetime64('NaT') # pragma: no cover
result = np.array([iNaT, '2000-01-01T00:00:00.000000000'], dtype='M8[ns]') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
from l3.Runtime import _l_
arr = np.array(["1/1/1000", "1/1/2000"], dtype=object)
_l_(10616)
result, _ = tslib.array_to_datetime(arr, errors="coerce")
_l_(10617)

expected = [iNaT, "2000-01-01T00:00:00.000000000"]
_l_(10618)
expected = np.array(expected, dtype="M8[ns]")
_l_(10619)

tm.assert_numpy_array_equal(result, expected)
_l_(10620)
