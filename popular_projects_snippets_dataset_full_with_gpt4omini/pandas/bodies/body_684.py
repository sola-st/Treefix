# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH50047
arr = np.array([True, False, val], dtype=object)
exp = BooleanArray(
    np.array([True, False, False]), np.array([False, False, True])
)
out = lib.maybe_convert_objects(arr, convert_to_nullable_dtype=True)
tm.assert_extension_array_equal(out, exp)
