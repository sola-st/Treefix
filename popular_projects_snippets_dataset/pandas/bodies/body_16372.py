# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
data = dict_subclass((x, 10.0 * x) for x in range(10))
series = Series(data)
expected = Series(dict(data.items()))
tm.assert_series_equal(series, expected)
