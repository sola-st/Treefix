# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
arr = SparseArray([1, 0, 0, 0, 2], kind="integer")
result = arr.nbytes
# (2 * 8) + 2 * 4
assert result == 24
