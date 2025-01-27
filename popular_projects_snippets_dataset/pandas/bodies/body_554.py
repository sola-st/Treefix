# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_downcast.py
dtype = klass.__name__ + "[ns]"
arr = np.array([1, 2, np.nan])

exp = np.array([1, 2, klass("NaT")], dtype)
res = maybe_downcast_to_dtype(arr, dtype)
tm.assert_numpy_array_equal(res, exp)
