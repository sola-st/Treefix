# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH19406
ser = Series([None, "b", None])
mask = func([True, False, True])
ser[mask] = ["a", "c"]
expected = Series(["a", "b", "c"])
tm.assert_series_equal(ser, expected)
