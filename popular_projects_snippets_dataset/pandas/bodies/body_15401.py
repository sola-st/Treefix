# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#12599
ser = Series(dtype=object)
ser["a"] = Timestamp("2016-01-01")
ser["b"] = 3.0
ser["c"] = "foo"
expected = Series([Timestamp("2016-01-01"), 3.0, "foo"], index=["a", "b", "c"])
tm.assert_series_equal(ser, expected)
