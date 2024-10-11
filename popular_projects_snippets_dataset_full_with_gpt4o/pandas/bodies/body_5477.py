# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert ts.max >= ts
assert ts.max._creso == ts._creso
assert ts.max.value == np.iinfo(np.int64).max
