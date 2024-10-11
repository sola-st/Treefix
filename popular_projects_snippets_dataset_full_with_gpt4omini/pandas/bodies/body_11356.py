# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: taking a subset of the rows of a DataFrame using a slice
# + afterwards modifying the subset
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()

subset = df[1:3]
subset._mgr._verify_integrity()

assert np.shares_memory(get_array(subset, "a"), get_array(df, "a"))

if using_copy_on_write:
    subset.iloc[0, 0] = 0
    assert not np.shares_memory(get_array(subset, "a"), get_array(df, "a"))

else:
    # INFO this no longer raise warning since pandas 1.4
    # with pd.option_context("chained_assignment", "warn"):
    #     with tm.assert_produces_warning(SettingWithCopyWarning):
    subset.iloc[0, 0] = 0

subset._mgr._verify_integrity()

expected = DataFrame({"a": [0, 3], "b": [5, 6], "c": [0.2, 0.3]}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    # original parent dataframe is not modified (CoW)
    tm.assert_frame_equal(df, df_orig)
else:
    # original parent dataframe is actually updated
    df_orig.iloc[1, 0] = 0
    tm.assert_frame_equal(df, df_orig)
