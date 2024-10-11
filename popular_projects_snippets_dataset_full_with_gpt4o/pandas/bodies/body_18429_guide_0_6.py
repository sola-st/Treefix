import numpy as np # pragma: no cover
import pytest # pragma: no cover
from pandas import date_range # pragma: no cover
import pandas.testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22074
# reversion test that we _don't_ call _assert_tzawareness_compat
# when comparing against TimedeltaIndex
from l3.Runtime import _l_
dti = date_range("2000-01-01", periods=10, tz="Asia/Tokyo")
_l_(20903)

result = dti == other
_l_(20904)
expected = np.array([False] * 10)
_l_(20905)
tm.assert_numpy_array_equal(result, expected)
_l_(20906)

result = dti != other
_l_(20907)
expected = np.array([True] * 10)
_l_(20908)
tm.assert_numpy_array_equal(result, expected)
_l_(20909)
msg = "Invalid comparison between"
_l_(20910)
with pytest.raises(TypeError, match=msg):
    _l_(20912)

    dti < other
    _l_(20911)
with pytest.raises(TypeError, match=msg):
    _l_(20914)

    dti <= other
    _l_(20913)
with pytest.raises(TypeError, match=msg):
    _l_(20916)

    dti > other
    _l_(20915)
with pytest.raises(TypeError, match=msg):
    _l_(20918)

    dti >= other
    _l_(20917)
