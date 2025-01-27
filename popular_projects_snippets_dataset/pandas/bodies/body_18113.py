# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx = period_range("2007-01", periods=20, freq="M")
per = idx[10]

result = idx < per
exp = idx.values < idx.values[10]
tm.assert_numpy_array_equal(result, exp)

# Tests Period.__richcmp__ against ndarray[object, ndim=2]
result = idx.values.reshape(10, 2) < per
tm.assert_numpy_array_equal(result, exp.reshape(10, 2))

# Tests Period.__richcmp__ against ndarray[object, ndim=0]
result = idx < np.array(per)
tm.assert_numpy_array_equal(result, exp)
