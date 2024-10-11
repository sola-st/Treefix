# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH#45778
ser = Series([1, 2], index=["a", "b"])
expected = ser.copy()
rhs = Series([6, 7], index=["a", "b"])
ser.loc[ser > 100] = rhs
tm.assert_series_equal(ser, expected)
