# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Return the minimum value of the Array or minimum along
        an axis.

        See Also
        --------
        numpy.ndarray.min
        Index.min : Return the minimum value in an Index.
        Series.min : Return the minimum value in a Series.
        """
nv.validate_min((), kwargs)
nv.validate_minmax_axis(axis, self.ndim)

result = nanops.nanmin(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
