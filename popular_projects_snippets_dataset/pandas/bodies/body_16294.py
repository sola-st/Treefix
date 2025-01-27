# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
s = Series(None, index=range(5))
assert s.dtype == np.float64

s = Series(None, index=range(5), dtype=object)
assert s.dtype == np.object_

# GH 7431
# inference on the index
s = Series(index=np.array([None]))
expected = Series(index=Index([None]))
tm.assert_series_equal(s, expected)
