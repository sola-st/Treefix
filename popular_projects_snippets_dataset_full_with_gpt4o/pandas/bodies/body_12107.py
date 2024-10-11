# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_upcast.py
# GH#36712
dtype = np.int64
na_value = na_values[dtype]
arr = np.array([na_value, na_value], dtype=dtype)
result = _maybe_upcast(arr, use_nullable_dtypes=True)

expected_mask = np.array([True, True])
expected = IntegerArray(arr, mask=expected_mask)
tm.assert_extension_array_equal(result, expected)
