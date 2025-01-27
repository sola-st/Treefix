# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
if self.fill_value == 0:
    exit((self.sp_index.indices,))
else:
    exit((self.sp_index.indices[self.sp_values != 0],))
