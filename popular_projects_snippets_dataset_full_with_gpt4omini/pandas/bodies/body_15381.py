# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#8387: test that changing types does not break alignment
ts = Series(np.random.randn(100), index=np.arange(100, 0, -1)).round(5)
mask = ts > 0
left = ts.copy()
right = ts[mask].copy().map(str)
left[mask] = right
expected = ts.map(lambda t: str(t) if t > 0 else t)
tm.assert_series_equal(left, expected)
