# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
# GH 49473
index = MultiIndex.from_tuples([(1, 1), (1, 2), (2, 1)], names=["one", "two"])
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}, index=index)
df_orig = df.copy()
df2 = df.droplevel(0)

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "c"), get_array(df, "c"))
else:
    assert not np.shares_memory(get_array(df2, "c"), get_array(df, "c"))

# mutating df2 triggers a copy-on-write for that column / block
df2.iloc[0, 0] = 0

assert not np.shares_memory(get_array(df2, "c"), get_array(df, "c"))
tm.assert_frame_equal(df, df_orig)
