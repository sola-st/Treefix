# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# with empty series (#4651)
s = Series([], dtype=np.int64, name=name)
assert repr(s) == expected
