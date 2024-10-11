# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH 7173
s = Series([1.0, 2.0, 3.0])
result = s.interpolate(limit=1)
expected = s
tm.assert_series_equal(result, expected)
