# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
sparray = SparseArray([0, 2, 0, 0])
ndarray = np.array([0, 1, 2, 3])
ndarray += sparray
expected = np.array([0, 3, 2, 3])
tm.assert_numpy_array_equal(ndarray, expected)
