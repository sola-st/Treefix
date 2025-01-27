# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
arr = SparseArray([0, 1, 2])
res = arr[[False, False, False]]
assert res.dtype == arr.dtype
