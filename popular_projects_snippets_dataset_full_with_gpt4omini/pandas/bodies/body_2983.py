# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH 14773
df = DataFrame(range(5))
df = df.astype(any_int_numpy_dtype)
result = df.diff()
expected_dtype = (
    "float32" if any_int_numpy_dtype in ("int8", "int16") else "float64"
)
expected = DataFrame([np.nan, 1.0, 1.0, 1.0, 1.0], dtype=expected_dtype)
tm.assert_frame_equal(result, expected)
