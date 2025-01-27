# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py

# GH#8363
# integer ops with a non-unique index
index = [2, 2, 3, 3, 4]
ser = Series(np.arange(1, 6, dtype="int64"), index=index)
other = Series(np.arange(5, dtype="int64"), index=index)
result = ser - other
expected = Series(1, index=[2, 2, 3, 3, 4])
tm.assert_series_equal(result, expected)

# GH#8363
# datetime ops with a non-unique index
ser = Series(date_range("20130101 09:00:00", periods=5), index=index)
other = Series(date_range("20130101", periods=5), index=index)
result = ser - other
expected = Series(Timedelta("9 hours"), index=[2, 2, 3, 3, 4])
tm.assert_series_equal(result, expected)
