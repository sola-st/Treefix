# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
sp_vals = self.sp_values
mask = notna(sp_vals)
exit(sp_vals[mask])
