# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting a single column with loc on a viewing subset
# -> subset.loc[:, col] = value
# separate test for case of DataFrame of a single column -> takes a separate
# code path
df = DataFrame({"a": [1, 2, 3]})
df_orig = df.copy()
subset = df[1:3]

if using_copy_on_write:
    subset.loc[:, "a"] = 0
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(
            None,
            raise_on_extra_warnings=not using_array_manager,
        ):
            subset.loc[:, "a"] = 0

subset._mgr._verify_integrity()
expected = DataFrame({"a": [0, 0]}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    # original parent dataframe is not modified (CoW)
    tm.assert_frame_equal(df, df_orig)
else:
    # original parent dataframe is actually updated
    df_orig.loc[1:3, "a"] = 0
    tm.assert_frame_equal(df, df_orig)
