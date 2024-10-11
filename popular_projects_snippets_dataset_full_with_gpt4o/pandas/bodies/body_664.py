# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([2**63], dtype=object)
exp = np.array([2**63], dtype=np.uint64)
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)

arr = np.array([str(2**63)], dtype=object)
exp = np.array([2**63], dtype=np.uint64)
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)

arr = np.array([np.uint64(2**63)], dtype=object)
exp = np.array([2**63], dtype=np.uint64)
tm.assert_numpy_array_equal(lib.maybe_convert_numeric(arr, set())[0], exp)
