import pandas as pd # pragma: no cover
from pandas import Series, date_range # pragma: no cover
from pandas.testing import assert_series_equal # pragma: no cover

box = pd.Index # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': assert_series_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#33404 fall back to positional since ints are unambiguous
from l3.Runtime import _l_
dti = date_range("2000-01-03", periods=3)._with_freq(None)
_l_(21641)
ii = pd.IntervalIndex.from_breaks(dti)
_l_(21642)
ser = Series(range(len(ii)), index=ii)
_l_(21643)

expected = ser.iloc[:1]
_l_(21644)
key = box([0])
_l_(21645)
result = ser[key]
_l_(21646)
tm.assert_series_equal(result, expected)
_l_(21647)
