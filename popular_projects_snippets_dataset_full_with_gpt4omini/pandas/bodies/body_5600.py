# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
s = Series([1, 2, 2**63, 2**63], dtype=np.uint64)
exp = np.array([1, 2, 2**63], dtype=np.uint64)
tm.assert_numpy_array_equal(algos.unique(s), exp)
