# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: taking a subset of the columns of a DataFrame using a slice
# + afterwards modifying the subset
single_block = (dtype == "int64") and not using_array_manager
df = DataFrame(
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": np.array([7, 8, 9], dtype=dtype)}
)
df_orig = df.copy()

subset = df.iloc[:, 1:]
subset._mgr._verify_integrity()

if using_copy_on_write:
    assert np.shares_memory(get_array(subset, "b"), get_array(df, "b"))

    subset.iloc[0, 0] = 0
    assert not np.shares_memory(get_array(subset, "b"), get_array(df, "b"))

else:
    # we only get a warning in case of a single block
    warn = SettingWithCopyWarning if single_block else None
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(warn):
            subset.iloc[0, 0] = 0

expected = DataFrame({"b": [0, 5, 6], "c": np.array([7, 8, 9], dtype=dtype)})
tm.assert_frame_equal(subset, expected)
# original parent dataframe is not modified (also not for BlockManager case,
# except for single block)
if not using_copy_on_write and (using_array_manager or single_block):
    df_orig.iloc[0, 1] = 0
    tm.assert_frame_equal(df, df_orig)
else:
    tm.assert_frame_equal(df, df_orig)
