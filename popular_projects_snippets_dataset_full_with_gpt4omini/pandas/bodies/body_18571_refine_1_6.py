import numpy as np # pragma: no cover
from pandas._libs.tslibs import NaT as iNaT # pragma: no cover
import pandas.testing as tm # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas._libs.tslibs import NaT as iNaT # pragma: no cover
import pandas.testing as tm # pragma: no cover

tslib = pd._libs.tslibs # pragma: no cover
iNaT = tslib.NaT # pragma: no cover
tm = pd.testing # pragma: no cover

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
