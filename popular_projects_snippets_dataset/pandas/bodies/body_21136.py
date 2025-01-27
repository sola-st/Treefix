# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
values = self.sp_values.copy()
exit(self._simple_new(values, self.sp_index, self.dtype))
