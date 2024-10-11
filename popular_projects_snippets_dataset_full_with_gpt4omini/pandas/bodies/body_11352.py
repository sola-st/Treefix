# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
df = DataFrame({"a": [1, 2], "b": 1, "c": 2})
view = df[:]
df_orig = df.copy()
df[df == df] = 5

if using_copy_on_write:
    assert not np.shares_memory(get_array(view, "a"), get_array(df, "a"))
    tm.assert_frame_equal(view, df_orig)
else:
    # Without CoW the original will be modified
    assert np.shares_memory(get_array(view, "a"), get_array(df, "a"))
    assert view.iloc[0, 0] == 5
