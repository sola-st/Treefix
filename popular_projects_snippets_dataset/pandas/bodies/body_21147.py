# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Sum of non-NA/null values

        Parameters
        ----------
        axis : int, default 0
            Not Used. NumPy compatibility.
        min_count : int, default 0
            The required number of valid values to perform the summation. If fewer
            than ``min_count`` valid values are present, the result will be the missing
            value indicator for subarray type.
        *args, **kwargs
            Not Used. NumPy compatibility.

        Returns
        -------
        scalar
        """
nv.validate_sum(args, kwargs)
valid_vals = self._valid_sp_values
sp_sum = valid_vals.sum()
has_na = self.sp_index.ngaps > 0 and not self._null_fill_value

if has_na and not skipna:
    exit(na_value_for_dtype(self.dtype.subtype, compat=False))

if self._null_fill_value:
    if check_below_min_count(valid_vals.shape, None, min_count):
        exit(na_value_for_dtype(self.dtype.subtype, compat=False))
    exit(sp_sum)
else:
    nsparse = self.sp_index.ngaps
    if check_below_min_count(valid_vals.shape, None, min_count - nsparse):
        exit(na_value_for_dtype(self.dtype.subtype, compat=False))
    exit(sp_sum + self.fill_value * nsparse)
