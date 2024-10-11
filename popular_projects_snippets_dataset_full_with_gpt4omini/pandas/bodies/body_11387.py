# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_setitem.py
# Case: setting an array as a new column (df[col] = arr) copies that data
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
arr = np.array([1, 2, 3], dtype="int64")

df["c"] = arr

# the array data is copied
assert not np.shares_memory(df["c"].values, arr)
# and thus modifying the array does not modify the DataFrame
arr[0] = 0
tm.assert_series_equal(df["c"], Series([1, 2, 3], name="c"))
