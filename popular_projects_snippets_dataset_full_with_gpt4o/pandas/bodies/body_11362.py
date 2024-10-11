# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting a single column on a viewing subset -> subset[col] = value
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]})
df_orig = df.copy()
subset = df[1:3]

if using_copy_on_write:
    subset["a"] = np.array([10, 11], dtype="int64")
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(SettingWithCopyWarning):
            subset["a"] = np.array([10, 11], dtype="int64")

subset._mgr._verify_integrity()
expected = DataFrame(
    {"a": [10, 11], "b": [5, 6], "c": [0.2, 0.3]}, index=range(1, 3)
)
tm.assert_frame_equal(subset, expected)
tm.assert_frame_equal(df, df_orig)
