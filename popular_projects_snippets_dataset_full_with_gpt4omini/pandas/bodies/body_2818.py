# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#48184
df = DataFrame({"a": [1, 2], "b": [1, 2]}, dtype=any_unsigned_int_numpy_dtype)
result = df.reindex(columns=list("abcd"), index=[0, 1, 2, 3], fill_value=10)
expected = DataFrame(
    {"a": [1, 2, 10, 10], "b": [1, 2, 10, 10], "c": 10, "d": 10},
    dtype=any_unsigned_int_numpy_dtype,
)
tm.assert_frame_equal(result, expected)
