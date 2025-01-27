# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH 20734
index = Series(name="id", dtype="S24")
df = DataFrame(index=index)
df["a"] = Series(name="a", index=index, dtype=np.uint32)
df["b"] = Series(name="b", index=index, dtype="S64")
df["c"] = Series(name="c", index=index, dtype="S64")
df["d"] = Series(name="d", index=index, dtype=np.uint8)
result = df.dtypes
expected = Series([np.uint32, object, object, np.uint8], index=list("abcd"))
tm.assert_series_equal(result, expected)
