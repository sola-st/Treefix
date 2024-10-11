# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_setitem.py
# Case: setting an index as a new column (df[col] = idx) copies that data
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
idx = Index([1, 2, 3])

df["c"] = idx

# the index data is copied
assert not np.shares_memory(df["c"].values, idx.values)

# and thus modifying the index does not modify the DataFrame
idx.values[0] = 0
tm.assert_series_equal(df["c"], Series([1, 2, 3], name="c"))

idx = RangeIndex(1, 4)
arr = idx.values

df["d"] = idx

assert not np.shares_memory(df["d"].values, arr)
arr[0] = 0
tm.assert_series_equal(df["d"], Series([1, 2, 3], name="d"))
