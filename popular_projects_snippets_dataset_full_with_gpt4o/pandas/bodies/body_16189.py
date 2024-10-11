# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#22962
ser = Series([1, None, 3], dtype="Int64")
result = ser + [1, None, val]
expected = Series([2, None, 3 + val], dtype=dtype)
tm.assert_series_equal(result, expected)

result = [1, None, val] + ser
tm.assert_series_equal(result, expected)
