# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
s = Series(range(3))
s2 = s.map(lambda x: np.where(x == 0, 0, 1))
assert issubclass(s2.dtype.type, np.integer)
