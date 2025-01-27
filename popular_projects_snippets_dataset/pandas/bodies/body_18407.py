# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
# GH #28981
expected = Series([False, False])
s = Series([Interval(0, 1), Interval(1, 2)], dtype="interval")
result = s == scalars
tm.assert_series_equal(result, expected)
