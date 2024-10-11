# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3]})
df_orig = df.copy()
df2 = method(df)
df2._mgr._verify_integrity()

if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
    assert np.shares_memory(get_array(df2, "b"), get_array(df, "b"))

# modify df2 to trigger CoW for that block
df2.iloc[0, 0] = 0
assert np.shares_memory(get_array(df2, "b"), get_array(df, "b"))
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    # without CoW enabled, head and tail return views. Mutating df2 also mutates df.
    df2.iloc[0, 0] = 1
tm.assert_frame_equal(df, df_orig)
