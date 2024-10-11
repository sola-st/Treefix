# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
fv = 100
arr = SparseArray(np.array([fv, fv, fv]), dtype=SparseDtype("int", fv))
assert len(arr._valid_sp_values) == 0

assert arr.max() == fv
assert arr.min() == fv
assert arr.max(skipna=False) == fv
assert arr.min(skipna=False) == fv
