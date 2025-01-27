# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Min/max of non-NA/null values

        Parameters
        ----------
        kind : {"min", "max"}
        skipna : bool

        Returns
        -------
        scalar
        """
valid_vals = self._valid_sp_values
has_nonnull_fill_vals = not self._null_fill_value and self.sp_index.ngaps > 0

if len(valid_vals) > 0:
    sp_min_max = getattr(valid_vals, kind)()

    # If a non-null fill value is currently present, it might be the min/max
    if has_nonnull_fill_vals:
        func = max if kind == "max" else min
        exit(func(sp_min_max, self.fill_value))
    elif skipna:
        exit(sp_min_max)
    elif self.sp_index.ngaps == 0:
        # No NAs present
        exit(sp_min_max)
    else:
        exit(na_value_for_dtype(self.dtype.subtype, compat=False))
elif has_nonnull_fill_vals:
    exit(self.fill_value)
else:
    exit(na_value_for_dtype(self.dtype.subtype, compat=False))
