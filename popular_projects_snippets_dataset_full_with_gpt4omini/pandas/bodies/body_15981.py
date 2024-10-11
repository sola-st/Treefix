# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# partial dict
ser = Series(np.arange(4), index=["a", "b", "c", "d"], dtype="int64")
renamed = ser.rename({"b": "foo", "d": "bar"})
tm.assert_index_equal(renamed.index, Index(["a", "foo", "c", "bar"]))
