import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pandas._libs.tslibs as tslib # pragma: no cover

iNaT = pd.NaT # pragma: no cover
np = type('Mock', (object,), {'array': np.array})() # pragma: no cover
tm = type('Mock', (object,), {'assert_numpy_array_equal': staticmethod(lambda x, y: np.testing.assert_array_equal(x, y))})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

iNaT = pd.NaT # pragma: no cover
def mock_array_to_datetime(arr, errors): return pd.to_datetime(arr, errors=errors).to_numpy(), None # pragma: no cover
tslib = type('Mock', (object,), {'array_to_datetime': staticmethod(mock_array_to_datetime)})() # pragma: no cover
tm = type('Mock', (object,), {'assert_numpy_array_equal': staticmethod(lambda x, y: np.testing.assert_array_equal(x, y))})() # pragma: no cover

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
