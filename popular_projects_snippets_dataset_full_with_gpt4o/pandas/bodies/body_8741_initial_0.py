import pandas as pd # pragma: no cover
from pandas import PeriodIndex # pragma: no cover
import numpy as np # pragma: no cover

self = type('Mock', (object,), {'index_cls': pd.Index})() # pragma: no cover
arr1d = pd.period_range(start='2021-01-01', periods=5, freq='D') # pragma: no cover
pd = pd # pragma: no cover
PeriodIndex = pd.PeriodIndex # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
from l3.Runtime import _l_
pi = self.index_cls(arr1d)
_l_(17716)
arr = arr1d
_l_(17717)
assert list(arr) == list(pi)
_l_(17718)

# Check that Index.__new__ knows what to do with PeriodArray
pi2 = pd.Index(arr)
_l_(17719)
assert isinstance(pi2, PeriodIndex)
_l_(17720)
assert list(pi2) == list(arr)
_l_(17721)
