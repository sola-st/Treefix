# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([0, 1, np.nan, 3])
result = s.interpolate(**kwargs)
expected = Series([0.0, 1.0, 2.0, 3.0])
tm.assert_series_equal(result, expected)
