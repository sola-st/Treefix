# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
result = SparseArray(arr, fill_value=fill_value)._first_fill_value_loc()
assert result == loc
