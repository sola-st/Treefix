# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
# Case: selecting columns using `filter()` returns a new dataframe
# + afterwards modifying the result
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()
df2 = df.filter(**filter_kwargs)
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))

# mutating df2 triggers a copy-on-write for that column/block
if using_copy_on_write:
    df2.iloc[0, 0] = 0
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
tm.assert_frame_equal(df, df_orig)
