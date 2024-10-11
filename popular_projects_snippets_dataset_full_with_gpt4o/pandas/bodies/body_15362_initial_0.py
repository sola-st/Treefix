from pandas import Series # pragma: no cover

index_vals = ['a', 'b', 'c', 'd', 'e'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH 11747
from l3.Runtime import _l_
s = Series(range(5), index=list(index_vals))
_l_(21175)
result = s[3]
_l_(21176)
assert result == 3
_l_(21177)
