# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting values with a mask on a viewing subset: subset[mask] = value
df = DataFrame({"a": [1, 2, 3, 4], "b": [4, 5, 6, 7], "c": [0.1, 0.2, 0.3, 0.4]})
df_orig = df.copy()
subset = df[1:4]

mask = subset > 3

if using_copy_on_write:
    subset[mask] = 0
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(SettingWithCopyWarning):
            subset[mask] = 0

expected = DataFrame(
    {"a": [2, 3, 0], "b": [0, 0, 0], "c": [0.20, 0.3, 0.4]}, index=range(1, 4)
)
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    # original parent dataframe is not modified (CoW)
    tm.assert_frame_equal(df, df_orig)
else:
    # original parent dataframe is actually updated
    df_orig.loc[3, "a"] = 0
    df_orig.loc[1:3, "b"] = 0
    tm.assert_frame_equal(df, df_orig)
