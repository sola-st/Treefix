# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_arithmetic.py
a = pd.array([-1, 0, 1, None, 2], dtype=dtype)
result = a**0
expected = pd.array([1, 1, 1, 1, 1], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = a**1
expected = pd.array([-1, 0, 1, None, 2], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = a**pd.NA
expected = pd.array([None, None, 1, None, None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = a**np.nan
# TODO np.nan should be converted to pd.NA / missing before operation?
expected = FloatingArray(
    np.array([np.nan, np.nan, 1, np.nan, np.nan], dtype=dtype.numpy_dtype),
    mask=a._mask,
)
tm.assert_extension_array_equal(result, expected)

# reversed
a = a[1:]  # Can't raise integers to negative powers.

result = 0**a
expected = pd.array([1, 0, None, 0], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = 1**a
expected = pd.array([1, 1, 1, 1], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = pd.NA**a
expected = pd.array([1, None, None, None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)

result = np.nan**a
expected = FloatingArray(
    np.array([1, np.nan, np.nan, np.nan], dtype=dtype.numpy_dtype), mask=a._mask
)
tm.assert_extension_array_equal(result, expected)
