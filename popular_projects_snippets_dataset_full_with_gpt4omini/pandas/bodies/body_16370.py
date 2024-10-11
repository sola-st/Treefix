# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/36291
n = 1_000_000_000_000_000_000_000
result = Series(n, index=[0])
expected = Series(n)
tm.assert_series_equal(result, expected)
