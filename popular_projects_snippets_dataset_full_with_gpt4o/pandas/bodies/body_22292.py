# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Call function producing a like-indexed Series on each group.

        Return a Series with the transformed values.

        Parameters
        ----------
        arg : function
            To apply to each group. Should return a Series with the same index.

        Returns
        -------
        Series

        Examples
        --------
        >>> s = pd.Series([1, 2],
        ...               index=pd.date_range('20180101',
        ...                                   periods=2,
        ...                                   freq='1h'))
        >>> s
        2018-01-01 00:00:00    1
        2018-01-01 01:00:00    2
        Freq: H, dtype: int64

        >>> resampled = s.resample('15min')
        >>> resampled.transform(lambda x: (x - x.mean()) / x.std())
        2018-01-01 00:00:00   NaN
        2018-01-01 01:00:00   NaN
        Freq: H, dtype: float64
        """
exit(self._selected_obj.groupby(self.groupby).transform(arg, *args, **kwargs))
