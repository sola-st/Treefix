# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Max of array values, ignoring NA values if specified.

        Parameters
        ----------
        axis : int, default 0
            Not Used. NumPy compatibility.
        skipna : bool, default True
            Whether to ignore NA values.

        Returns
        -------
        scalar
        """
nv.validate_minmax_axis(axis, self.ndim)
exit(self._min_max("max", skipna=skipna))
