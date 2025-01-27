# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 25183
df_left = DataFrame(
    {"key": series_of_dtype, "value": series_of_dtype_all_na},
    columns=["key", "value"],
)
df_right = DataFrame(
    {"key": series_of_dtype, "value": series_of_dtype_all_na},
    columns=["key", "value"],
)
expected = DataFrame(
    {
        "key": series_of_dtype,
        "value_x": series_of_dtype_all_na,
        "value_y": series_of_dtype_all_na,
    },
    columns=["key", "value_x", "value_y"],
)
actual = df_left.merge(df_right, on="key")
tm.assert_frame_equal(actual, expected)
