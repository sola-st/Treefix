# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#38148
df = DataFrame({"a": [1, 2, 3], "b": [4, 4, 6]})

# get one column as a view of df
ser = df["a"]

# add columns with list-like indexer
df[["c", "d"]] = np.array([[0.1, 0.2], [0.3, 0.4], [0.4, 0.5]])

# edit in place the first column to check view semantics
df.iloc[0, 0] = 100

if using_copy_on_write:
    expected = Series([1, 2, 3], name="a")
else:
    expected = Series([100, 2, 3], name="a")
tm.assert_series_equal(ser, expected)
