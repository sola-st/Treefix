# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_duplicated.py
# GH#48150
ser = Series([1, 2, NA], dtype="Int64")
result = ser.duplicated(keep=keep)
expected = Series([False, False, False])
tm.assert_series_equal(result, expected)
