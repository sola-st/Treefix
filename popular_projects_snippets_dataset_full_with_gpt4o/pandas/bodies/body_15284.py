# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH#50161
ser = Series(1, index=Index([0, 1, 2], dtype="Int64"))
result = ser.loc[2:3]
expected = Series(1, index=Index([2], dtype="Int64"))
tm.assert_series_equal(result, expected)
