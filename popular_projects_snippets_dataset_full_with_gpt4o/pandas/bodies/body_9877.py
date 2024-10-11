# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH#42452
df = DataFrame({"A": range(5), "B": range(10, 15)}, dtype=float_numpy_dtype)
expected = DataFrame(
    {"A": [np.nan] * 5, "B": range(10, 20, 2)},
    dtype=float_numpy_dtype,
)
result = df.rolling(2, axis=1).sum()
tm.assert_frame_equal(result, expected, check_dtype=False)
