# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH#50043
arr = np.array([val, None, 3], dtype="object")
result = lib.maybe_convert_objects(arr, convert_to_nullable_dtype=True)
expected = IntegerArray(
    np.array([val, 0, 3], dtype=dtype), np.array([False, True, False])
)
tm.assert_extension_array_equal(result, expected)
