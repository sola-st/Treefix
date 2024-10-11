# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Return sample standard deviation over requested axis.

        Normalized by N-1 by default. This can be changed using the ddof argument

        Parameters
        ----------
        axis : int optional, default None
            Axis for the function to be applied on.
            For `Series` this parameter is unused and defaults to `None`.
        ddof : int, default 1
            Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.
        skipna : bool, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be
            NA.

        Returns
        -------
        Timedelta
        """
# Because std is translation-invariant, we can get self.std
#  by calculating (self - Timestamp(0)).std, and we can do it
#  without creating a copy by using a view on self._ndarray
from pandas.core.arrays import TimedeltaArray

# Find the td64 dtype with the same resolution as our dt64 dtype
dtype_str = self._ndarray.dtype.name.replace("datetime64", "timedelta64")
dtype = np.dtype(dtype_str)

tda = TimedeltaArray._simple_new(self._ndarray.view(dtype), dtype=dtype)

exit(tda.std(axis=axis, out=out, ddof=ddof, keepdims=keepdims, skipna=skipna))
