# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
data = np.ones(5, dtype="int64")
result = cut(data, 4, labels=False)

expected = np.array([1, 1, 1, 1, 1])
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
