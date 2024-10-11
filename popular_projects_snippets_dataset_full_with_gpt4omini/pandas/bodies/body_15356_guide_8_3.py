import pandas as pd # pragma: no cover

string_series = pd.Series(['alpha', 'beta', 'gamma', 'delta'], index=[0, 1, 2, 3]) # pragma: no cover
object_series = pd.Series([10, 20, 30, 40], index=[0, 1, 2, 3]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
from l3.Runtime import _l_
slice1 = string_series[[1, 2, 3]]
_l_(4175)
slice2 = object_series[[1, 2, 3]]
_l_(4176)
assert string_series.index[2] == slice1.index[1]
_l_(4177)
assert object_series.index[2] == slice2.index[1]
_l_(4178)
assert string_series[2] == slice1[1]
_l_(4179)
assert object_series[2] == slice2[1]
_l_(4180)
