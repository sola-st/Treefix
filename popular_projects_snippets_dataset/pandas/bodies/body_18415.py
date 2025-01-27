# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
series = Series(date_range("1/1/2000", periods=10))

result = series > val
expected = Series([x > val for x in series])
tm.assert_series_equal(result, expected)
