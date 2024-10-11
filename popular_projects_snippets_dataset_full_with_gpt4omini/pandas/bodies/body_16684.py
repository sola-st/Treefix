# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 25183
df = DataFrame(
    {"key": series_of_dtype, "value": series_of_dtype2},
    columns=["key", "value"],
)
df_empty = df[:0]
expected = DataFrame(
    {
        "value_x": Series(dtype=df.dtypes["value"]),
        "key": Series(dtype=df.dtypes["key"]),
        "value_y": Series(dtype=df.dtypes["value"]),
    },
    columns=["value_x", "key", "value_y"],
)
actual = df_empty.merge(df, on="key")
tm.assert_frame_equal(actual, expected)
