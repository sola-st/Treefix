# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# Case where we hit a KeyError and then trying to set in-place incorrectly
#  casts a float to an int
ser = Series([1, 2, 3], index=["a", "b", "c"])
ser[0] = 1.5
expected = Series([1.5, 2, 3], index=["a", "b", "c"])
tm.assert_series_equal(ser, expected)
