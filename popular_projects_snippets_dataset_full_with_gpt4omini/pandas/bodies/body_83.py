# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
from l3.Runtime import _l_
left = Series({"a": 1.0, "b": 2.0, "c": 3.0, "d": 4})
_l_(10581)
right = Series({1: 11, 2: 22, 3: 33})
_l_(10582)

assert left.dtype == np.float_
_l_(10583)
assert issubclass(right.dtype.type, np.integer)
_l_(10584)

merged = left.map(right)
_l_(10585)
assert merged.dtype == np.float_
_l_(10586)
assert isna(merged["d"])
_l_(10587)
assert not isna(merged["c"])
_l_(10588)
