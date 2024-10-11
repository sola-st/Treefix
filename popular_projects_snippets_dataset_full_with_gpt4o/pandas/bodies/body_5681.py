# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# NaT - NaT is NaT, not 0
arr = np.arange(12).astype(np.int64).view(dtype).reshape(3, 4)
arr[:, 2] = arr.dtype.type("NaT", "ns")
result = algos.diff(arr, 1, axis=0)

expected = np.ones(arr.shape, dtype="timedelta64[ns]") * 4
expected[:, 2] = np.timedelta64("NaT", "ns")
expected[0, :] = np.timedelta64("NaT", "ns")

tm.assert_numpy_array_equal(result, expected)

result = algos.diff(arr.T, 1, axis=1)
tm.assert_numpy_array_equal(result, expected.T)
