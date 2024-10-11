import pandas as pd # pragma: no cover
from pandas import PeriodIndex # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.index_cls = pd.Index # pragma: no cover
arr1d = pd.array([1, 2, 3]) # pragma: no cover
PeriodIndex = pd.PeriodIndex # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
from l3.Runtime import _l_
pi = self.index_cls(arr1d)
_l_(5676)
arr = arr1d
_l_(5677)
assert list(arr) == list(pi)
_l_(5678)

# Check that Index.__new__ knows what to do with PeriodArray
pi2 = pd.Index(arr)
_l_(5679)
assert isinstance(pi2, PeriodIndex)
_l_(5680)
assert list(pi2) == list(arr)
_l_(5681)
