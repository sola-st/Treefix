# Extracted from ./data/repos/pandas/pandas/core/indexes/accessors.py
"""
        Return an array of native :class:`datetime.timedelta` objects.

        Python's standard `datetime` library uses a different representation
        timedelta's. This method converts a Series of pandas Timedeltas
        to `datetime.timedelta` format with the same length as the original
        Series.

        Returns
        -------
        numpy.ndarray
            Array of 1D containing data with `datetime.timedelta` type.

        See Also
        --------
        datetime.timedelta : A duration expressing the difference
            between two date, time, or datetime.

        Examples
        --------
        >>> s = pd.Series(pd.to_timedelta(np.arange(5), unit="d"))
        >>> s
        0   0 days
        1   1 days
        2   2 days
        3   3 days
        4   4 days
        dtype: timedelta64[ns]

        >>> s.dt.to_pytimedelta()
        array([datetime.timedelta(0), datetime.timedelta(days=1),
        datetime.timedelta(days=2), datetime.timedelta(days=3),
        datetime.timedelta(days=4)], dtype=object)
        """
exit(self._get_values().to_pytimedelta())
