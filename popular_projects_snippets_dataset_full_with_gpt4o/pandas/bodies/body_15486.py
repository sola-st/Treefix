# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#37692
ser = Series([1, 2, 3], index=["a", "b", "c"])
indexer_al(ser)["b"] = "test"
expected = Series([1, "test", 3], index=["a", "b", "c"], dtype=object)
tm.assert_series_equal(ser, expected)
