# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2], "b": "c"})
df2 = df.round()
df_orig = df.copy()

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "b"), get_array(df, "b"))
    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    assert not np.shares_memory(get_array(df2, "b"), get_array(df, "b"))

df2.iloc[0, 1] = "d"
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, "b"), get_array(df, "b"))
tm.assert_frame_equal(df, df_orig)
