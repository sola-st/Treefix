# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": "a"})
df_orig = df.copy()
df_changed = df[["b", "a"]].copy()
df2, _ = func(df, df_changed)

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))

df2.iloc[0, 0] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
tm.assert_frame_equal(df, df_orig)
