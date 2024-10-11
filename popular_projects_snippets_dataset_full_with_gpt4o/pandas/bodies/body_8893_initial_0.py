import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

IntervalArray = pd.arrays.IntervalArray # pragma: no cover
tm.assert_interval_array_equal = lambda x, y: (x, y) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# GH 25022
from l3.Runtime import _l_
arr = IntervalArray.from_tuples([(0, 1), (1, 2)])
_l_(22094)
result = repr(arr)
_l_(22095)
expected = (
    "<IntervalArray>\n"
    "[(0, 1], (1, 2]]\n"
    "Length: 2, dtype: interval[int64, right]"
)
_l_(22096)
assert result == expected
_l_(22097)
