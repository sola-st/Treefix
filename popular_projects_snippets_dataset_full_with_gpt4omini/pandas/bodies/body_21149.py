# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Mean of non-NA/null values

        Returns
        -------
        mean : float
        """
nv.validate_mean(args, kwargs)
valid_vals = self._valid_sp_values
sp_sum = valid_vals.sum()
ct = len(valid_vals)

if self._null_fill_value:
    exit(sp_sum / ct)
else:
    nsparse = self.sp_index.ngaps
    exit((sp_sum + self.fill_value * nsparse) / (ct + nsparse))
