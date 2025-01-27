# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#22962
ser = Series([True, None, False], dtype="boolean")
result = ser + [True, None, True]
expected = Series([True, None, True], dtype="boolean")
tm.assert_series_equal(result, expected)

result = [True, None, True] + ser
tm.assert_series_equal(result, expected)
