# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting a single column with loc on a viewing subset
# -> subset.loc[:, col] = value
df = DataFrame(
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": np.array([7, 8, 9], dtype=dtype)}
)
df_orig = df.copy()
subset = df[1:3]

if using_copy_on_write:
    subset.loc[:, "a"] = np.array([10, 11], dtype="int64")
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(
            None,
            raise_on_extra_warnings=not using_array_manager,
        ):
            subset.loc[:, "a"] = np.array([10, 11], dtype="int64")

subset._mgr._verify_integrity()
expected = DataFrame(
    {"a": [10, 11], "b": [5, 6], "c": np.array([8, 9], dtype=dtype)},
    index=range(1, 3),
)
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    # original parent dataframe is not modified (CoW)
    tm.assert_frame_equal(df, df_orig)
else:
    # original parent dataframe is actually updated
    df_orig.loc[1:3, "a"] = np.array([10, 11], dtype="int64")
    tm.assert_frame_equal(df, df_orig)
