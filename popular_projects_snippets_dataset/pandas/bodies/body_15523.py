# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
# GH#48304
ser = Series([1, 2, 2, 3])
result = ser.drop_duplicates(ignore_index=True)
expected = Series([1, 2, 3])
tm.assert_series_equal(result, expected)
