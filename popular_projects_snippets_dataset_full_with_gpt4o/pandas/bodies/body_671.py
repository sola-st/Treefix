# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array(value, dtype=object)
exp = np.array(value, dtype=expected_dtype)
tm.assert_numpy_array_equal(lib.maybe_convert_objects(arr), exp)
