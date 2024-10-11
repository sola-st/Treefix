# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
        Fill NA/NaN values using the specified method.

        Parameters
        ----------
        value : scalar, dict, Series
            If a scalar value is passed it is used to fill all missing values.
            Alternatively, a Series or dict can be used to fill in different
            values for each index. The value should not be a list. The
            value(s) passed should be either Interval objects or NA/NaN.
        method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
            (Not implemented yet for IntervalArray)
            Method to use for filling holes in reindexed Series
        limit : int, default None
            (Not implemented yet for IntervalArray)
            If method is specified, this is the maximum number of consecutive
            NaN values to forward/backward fill. In other words, if there is
            a gap with more than this number of consecutive NaNs, it will only
            be partially filled. If method is not specified, this is the
            maximum number of entries along the entire axis where NaNs will be
            filled.

        Returns
        -------
        filled : IntervalArray with NA/NaN filled
        """
if method is not None:
    raise TypeError("Filling by method is not supported for IntervalArray.")
if limit is not None:
    raise TypeError("limit is not supported for IntervalArray.")

value_left, value_right = self._validate_scalar(value)

left = self.left.fillna(value=value_left)
right = self.right.fillna(value=value_right)
exit(self._shallow_copy(left, right))
