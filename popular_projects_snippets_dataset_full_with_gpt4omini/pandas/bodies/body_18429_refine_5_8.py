import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import pandas._testing as tm # pragma: no cover

date_range = pd.date_range # pragma: no cover
other = pd.date_range('2000-01-01', periods=10, tz='UTC') # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import pandas.testing as tm # pragma: no cover

date_range = pd.date_range # pragma: no cover
other = pd.date_range('2000-01-01', periods=10, tz='Asia/Tokyo') # pragma: no cover
np = np # pragma: no cover
tm = tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22074
# reversion test that we _don't_ call _assert_tzawareness_compat
# when comparing against TimedeltaIndex
from l3.Runtime import _l_
dti = date_range("2000-01-01", periods=10, tz="Asia/Tokyo")
_l_(10177)

result = dti == other
_l_(10178)
expected = np.array([False] * 10)
_l_(10179)
tm.assert_numpy_array_equal(result, expected)
_l_(10180)

result = dti != other
_l_(10181)
expected = np.array([True] * 10)
_l_(10182)
tm.assert_numpy_array_equal(result, expected)
_l_(10183)
msg = "Invalid comparison between"
_l_(10184)
with pytest.raises(TypeError, match=msg):
    _l_(10186)

    dti < other
    _l_(10185)
with pytest.raises(TypeError, match=msg):
    _l_(10188)

    dti <= other
    _l_(10187)
with pytest.raises(TypeError, match=msg):
    _l_(10190)

    dti > other
    _l_(10189)
with pytest.raises(TypeError, match=msg):
    _l_(10192)

    dti >= other
    _l_(10191)
