# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
assert isinstance(res, SparseArray)
assert isinstance(res.dtype, SparseDtype)
assert res.dtype.subtype == np.bool_
assert isinstance(res.fill_value, bool)
