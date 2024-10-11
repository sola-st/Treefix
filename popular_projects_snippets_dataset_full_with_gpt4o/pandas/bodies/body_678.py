# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH27335
arr = np.array([2, np.NaN], dtype=object)
result = lib.maybe_convert_objects(arr, convert_to_nullable_dtype=True)

tm.assert_extension_array_equal(result, exp)
