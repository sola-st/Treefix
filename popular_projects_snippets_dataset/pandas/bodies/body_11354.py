# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: taking a subset of the columns of a DataFrame
# + afterwards modifying the subset
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()

subset = df[["a", "c"]]

if using_copy_on_write:
    # the subset shares memory ...
    assert np.shares_memory(get_array(subset, "a"), get_array(df, "a"))
    # ... but uses CoW when being modified
    subset.iloc[0, 0] = 0
else:
    assert not np.shares_memory(get_array(subset, "a"), get_array(df, "a"))
    # INFO this no longer raise warning since pandas 1.4
    # with pd.option_context("chained_assignment", "warn"):
    #     with tm.assert_produces_warning(SettingWithCopyWarning):
    subset.iloc[0, 0] = 0

assert not np.shares_memory(get_array(subset, "a"), get_array(df, "a"))

expected = DataFrame({"a": [0, 2, 3], "c": [0.1, 0.2, 0.3]})
tm.assert_frame_equal(subset, expected)
tm.assert_frame_equal(df, df_orig)
