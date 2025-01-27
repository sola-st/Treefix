# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#25338
ser = Series(["IntervalA", "IntervalB", "IntervalC"])
result = ser == "IntervalA"
expected = Series([True, False, False])
tm.assert_series_equal(result, expected)
