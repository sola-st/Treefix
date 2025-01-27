# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
# GH 49473
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()
df2 = df.set_index("a")

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "b"), get_array(df, "b"))
else:
    assert not np.shares_memory(get_array(df2, "b"), get_array(df, "b"))

# mutating df2 triggers a copy-on-write for that column / block
df2.iloc[0, 1] = 0
assert not np.shares_memory(get_array(df2, "c"), get_array(df, "c"))
tm.assert_frame_equal(df, df_orig)
