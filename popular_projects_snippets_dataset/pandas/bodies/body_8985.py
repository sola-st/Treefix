# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
arr2 = arr.copy()
assert arr2.sp_values is not arr.sp_values
assert arr2.sp_index is arr.sp_index
