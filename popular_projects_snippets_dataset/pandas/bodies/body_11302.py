# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
# Case: resetting the index (i.e. adding a new column) + mutating the
# resulting dataframe
df = DataFrame(
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]}, index=[10, 11, 12]
)
df_orig = df.copy()
df2 = df.reset_index()
df2._mgr._verify_integrity()

if using_copy_on_write:
    # still shares memory (df2 is a shallow copy)
    assert np.shares_memory(get_array(df2, "b"), get_array(df, "b"))
    assert np.shares_memory(get_array(df2, "c"), get_array(df, "c"))
# mutating df2 triggers a copy-on-write for that column / block
df2.iloc[0, 2] = 0
assert not np.shares_memory(get_array(df2, "b"), get_array(df, "b"))
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, "c"), get_array(df, "c"))
tm.assert_frame_equal(df, df_orig)
