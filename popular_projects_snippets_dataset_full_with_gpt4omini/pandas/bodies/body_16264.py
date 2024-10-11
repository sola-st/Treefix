# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 21987
expected = Series(list(range(10)), dtype="int64")
result = Series(range(10), dtype="int64")
tm.assert_series_equal(result, expected)
