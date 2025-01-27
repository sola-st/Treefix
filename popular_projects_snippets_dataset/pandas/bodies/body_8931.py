# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
sparray = SparseArray([0, 2, 0, 0])
ndarray = np.array([0, 1, 2, 3])
sparray += ndarray
expected = SparseArray([0, 3, 2, 3], fill_value=0)
tm.assert_sp_array_equal(sparray, expected)
