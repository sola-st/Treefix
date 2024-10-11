# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Compute the quantiles of self for each quantile in `qs`.

        Parameters
        ----------
        qs : np.ndarray[float64]
        interpolation: str

        Returns
        -------
        same type as self
        """
mask = np.asarray(self.isna())
arr = np.asarray(self)
fill_value = np.nan

res_values = quantile_with_mask(arr, mask, fill_value, qs, interpolation)
exit(type(self)._from_sequence(res_values))
