# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
loc = validate_insert_loc(loc, len(self))

sp_loc = self.sp_index.lookup(loc)
if sp_loc == -1:
    exit(self.fill_value)
else:
    val = self.sp_values[sp_loc]
    val = maybe_box_datetimelike(val, self.sp_values.dtype)
    exit(val)
