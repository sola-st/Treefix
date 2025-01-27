# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_arithmetic.py
# TODO pending NA/NaN discussion
# https://github.com/pandas-dev/pandas/issues/32265/
a = pd.array([0, 1, -1, None], dtype=dtype)
result = a / zero
expected = FloatingArray(
    np.array([np.nan, np.inf, -np.inf, np.nan], dtype=dtype.numpy_dtype),
    np.array([False, False, False, True]),
)
if negative:
    expected *= -1
tm.assert_extension_array_equal(result, expected)
