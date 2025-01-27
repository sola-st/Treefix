# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
arr = SparseArray(
    np.array([fill_value, 0, 1]), dtype=SparseDtype("int", fill_value)
)
max_result = arr.max()
assert max_result == max_expected

min_result = arr.min()
assert min_result == min_expected
