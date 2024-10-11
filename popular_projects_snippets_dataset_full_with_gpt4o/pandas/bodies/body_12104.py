# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_upcast.py
# GH#36712
if any_real_numpy_dtype == "float32":
    pytest.skip()

arr = np.array([1, 2, 3], dtype=any_real_numpy_dtype)
result = _maybe_upcast(arr, use_nullable_dtypes=True)

expected_mask = np.array([False, False, False])
if issubclass(np.dtype(any_real_numpy_dtype).type, np.integer):
    expected = IntegerArray(arr, mask=expected_mask)
else:
    expected = FloatingArray(arr, mask=expected_mask)

tm.assert_extension_array_equal(result, expected)
