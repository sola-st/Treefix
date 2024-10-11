# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH50047
arr = np.array([True, False], dtype=object)
exp = np.array([True, False])
out = lib.maybe_convert_objects(arr, convert_to_nullable_dtype=True)
tm.assert_numpy_array_equal(out, exp)

arr = np.array([True, False, pd.NaT], dtype=object)
exp = np.array([True, False, pd.NaT], dtype=object)
out = lib.maybe_convert_objects(arr, convert_to_nullable_dtype=True)
tm.assert_numpy_array_equal(out, exp)
