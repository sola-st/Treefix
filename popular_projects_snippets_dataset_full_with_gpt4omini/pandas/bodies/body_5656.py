# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = np.array([1, 2], dtype=np.float64)

s = Series([1, 2**63], dtype=dtype)
tm.assert_numpy_array_equal(algos.rank(s), exp)
