# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#12533
ser = Series([1, 2, 3, 4], index=list("ABCD"))
ser[lambda x: "A"] = -1

expected = Series([-1, 2, 3, 4], index=list("ABCD"))
tm.assert_series_equal(ser, expected)
