# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#45070 case where in __setitem__ we get a KeyError, then when
#  we fallback we *also* get a ValueError if we try to set inplace.
ser = Series([1, 2, 3], index=["a", "b", "c"])

ser[0] = "X"
expected = Series(["X", 2, 3], index=["a", "b", "c"], dtype=object)
tm.assert_series_equal(ser, expected)
