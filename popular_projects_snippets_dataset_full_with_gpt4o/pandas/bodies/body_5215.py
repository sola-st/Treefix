# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert td.max >= td
assert td.max._creso == td._creso
assert td.max.value == np.iinfo(np.int64).max
