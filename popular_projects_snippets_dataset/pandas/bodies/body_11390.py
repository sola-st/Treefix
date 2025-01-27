# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_setitem.py
# Case: setting a DataFrame as new columns copies that data
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df2 = DataFrame({"c": [7, 8, 9], "d": [10, 11, 12]})

df[["c", "d"]] = df2

if using_copy_on_write:
    # TODO(CoW) with CoW we can delay the copy
    # assert np.shares_memory(df["c"].values, df2["c"].values)
    assert not np.shares_memory(df["c"].values, df2["c"].values)
else:
    # the data is copied
    assert not np.shares_memory(df["c"].values, df2["c"].values)

# and modifying the set DataFrame does not modify the original DataFrame
df2.iloc[0, 0] = 0
tm.assert_series_equal(df["c"], Series([7, 8, 9], name="c"))
