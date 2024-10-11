import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas._libs import tslib # pragma: no cover
from pandas._libs.tslibs.nattype import iNaT # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
from l3.Runtime import _l_
arr = np.array(["1/1/1000", "1/1/2000"], dtype=object)
_l_(22000)
result, _ = tslib.array_to_datetime(arr, errors="coerce")
_l_(22001)

expected = [iNaT, "2000-01-01T00:00:00.000000000"]
_l_(22002)
expected = np.array(expected, dtype="M8[ns]")
_l_(22003)

tm.assert_numpy_array_equal(result, expected)
_l_(22004)
