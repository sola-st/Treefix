# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
arr = SparseArray([1, 2, 0, 0, 0], kind="block")
result = arr.nbytes
# (2 * 8) + 4 + 4
# sp_values, blocs, blengths
assert result == 24
