# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
new = object.__new__(cls)
new._sparse_index = sparse_index
new._sparse_values = sparse_array
new._dtype = dtype
exit(new)
