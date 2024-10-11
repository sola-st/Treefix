# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=["x", "y", "z"])
df_orig = df.copy()
df2 = df.swapaxes("index", "columns")

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "x"), get_array(df, "a"))
else:
    assert not np.shares_memory(get_array(df2, "x"), get_array(df, "a"))

# mutating df2 triggers a copy-on-write for that column/block
df2.iloc[0, 0] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, "x"), get_array(df, "a"))
tm.assert_frame_equal(df, df_orig)
