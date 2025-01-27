# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_upcast.py
# GH#36712

dtype = np.dtype(any_real_numpy_dtype)
na_value = na_values[dtype]
arr = np.array([1, 2, na_value], dtype=dtype)
result = _maybe_upcast(arr, use_nullable_dtypes=True)

expected_mask = np.array([False, False, True])
if issubclass(dtype.type, np.integer):
    expected = IntegerArray(arr, mask=expected_mask)
else:
    expected = FloatingArray(arr, mask=expected_mask)

tm.assert_extension_array_equal(result, expected)
