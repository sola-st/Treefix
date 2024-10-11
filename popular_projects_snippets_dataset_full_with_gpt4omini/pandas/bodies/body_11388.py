# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_setitem.py
# Case: setting a series as a new column (df[col] = s) copies that data
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
ser = Series([1, 2, 3])

df["c"] = ser

if using_copy_on_write:
    # TODO(CoW) with CoW we can delay the copy
    # assert np.shares_memory(df["c"].values, ser.values)
    assert not np.shares_memory(df["c"].values, ser.values)
else:
    # the series data is copied
    assert not np.shares_memory(df["c"].values, ser.values)

# and modifying the series does not modify the DataFrame
ser.iloc[0] = 0
assert ser.iloc[0] == 0
tm.assert_series_equal(df["c"], Series([1, 2, 3], name="c"))
