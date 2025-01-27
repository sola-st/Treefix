# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# if we are passed a scalar None, convert it here
if self.dtype != _dtype_obj and is_valid_na_for_dtype(value, self.dtype):
    value = self.fill_value
exit(value)
