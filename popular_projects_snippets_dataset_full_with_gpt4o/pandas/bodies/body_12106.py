# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_upcast.py
# GH#36712
dtype = np.bool_
arr = np.array([True, False, False], dtype="uint8").view(dtype)
result = _maybe_upcast(arr, use_nullable_dtypes=True)

expected_mask = np.array([False, False, False])
expected = BooleanArray(arr, mask=expected_mask)
tm.assert_extension_array_equal(result, expected)
