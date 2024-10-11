# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
index = MultiIndex.from_tuples(
    [(1, 1), (1, 2), (2, 1), (2, 2)], names=["one", "two"]
)
df = DataFrame({"a": [1, 2, 3, 4]}, index=index)
df_orig = df.copy()
df2 = df.reorder_levels(order=["two", "one"])

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))

df2.iloc[0, 0] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
tm.assert_frame_equal(df, df_orig)
