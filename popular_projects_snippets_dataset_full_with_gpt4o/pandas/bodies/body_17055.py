# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
df = DataFrame({"foo": [1, 2], "bar": [1, 2]}, dtype=df_dtype)
empty = DataFrame({"foo": [np.nan], "bar": [np.nan]}, dtype=empty_dtype)
result = concat([empty, df], ignore_index=True)

if df_dtype == "int64":
    # TODO what exact behaviour do we want for integer eventually?
    if empty_dtype == "object":
        df_dtype = "object"
    else:
        df_dtype = "float64"
expected = DataFrame({"foo": [None, 1, 2], "bar": [None, 1, 2]}, dtype=df_dtype)
tm.assert_frame_equal(result, expected)
