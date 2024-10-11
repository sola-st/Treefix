# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = Series([], dtype=np.float64, index=Index([], dtype=int))
tm.assert_numpy_array_equal(algos.mode([]), exp.values)
