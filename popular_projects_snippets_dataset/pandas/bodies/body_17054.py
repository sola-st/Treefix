# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# https://github.com/pandas-dev/pandas/issues/45637
df = DataFrame({"foo": [1, 2], "bar": [1, 2]}, dtype=df_dtype)
empty = DataFrame(columns=["foo", "bar"], dtype=empty_dtype)
result = concat([empty, df])
expected = df
if df_dtype == "int64":
    # TODO what exact behaviour do we want for integer eventually?
    if empty_dtype == "float64":
        expected = df.astype("float64")
    else:
        expected = df.astype("object")
tm.assert_frame_equal(result, expected)
