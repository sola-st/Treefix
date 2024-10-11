# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Return the maximum value of the Array or maximum along
        an axis.

        See Also
        --------
        numpy.ndarray.max
        Index.max : Return the maximum value in an Index.
        Series.max : Return the maximum value in a Series.
        """
nv.validate_max((), kwargs)
nv.validate_minmax_axis(axis, self.ndim)

result = nanops.nanmax(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
