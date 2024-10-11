# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting multiple columns on a viewing subset
# -> subset[[col1, col2]] = value
df = DataFrame(
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": np.array([7, 8, 9], dtype=dtype)}
)
df_orig = df.copy()
subset = df[1:3]

if using_copy_on_write:
    subset[["a", "c"]] = 0
else:
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(SettingWithCopyWarning):
            subset[["a", "c"]] = 0

subset._mgr._verify_integrity()
if using_copy_on_write:
    # first and third column should certainly have no references anymore
    assert all(subset._mgr._has_no_reference(i) for i in [0, 2])
expected = DataFrame({"a": [0, 0], "b": [5, 6], "c": [0, 0]}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
tm.assert_frame_equal(df, df_orig)
