# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unique.py
ser = Series([1, 2, 2**63, 2**63], dtype=np.uint64)
res = ser.unique()
exp = np.array([1, 2, 2**63], dtype=np.uint64)
tm.assert_numpy_array_equal(res, exp)
