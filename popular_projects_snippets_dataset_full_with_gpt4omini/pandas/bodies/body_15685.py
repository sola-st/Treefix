# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH 21037
ts = Series(data=[10, 9, np.nan, 2, 1], index=[10, 9, 3, 2, 1])
result = ts.sort_index(ascending=ascending).interpolate(method="index")
expected = Series(data=expected_values, index=expected_values, dtype=float)
tm.assert_series_equal(result, expected)
