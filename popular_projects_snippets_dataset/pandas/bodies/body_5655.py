# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = np.array([1, 2], dtype=np.float64)

data = np.array([1, 100], dtype=dtype)
data.setflags(write=writable)
ser = Series(data)
result = algos.rank(ser)
tm.assert_numpy_array_equal(result, exp)
