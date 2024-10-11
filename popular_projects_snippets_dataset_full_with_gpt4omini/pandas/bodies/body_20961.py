# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Return the day names with specified locale.

        Parameters
        ----------
        locale : str, optional
            Locale determining the language in which to return the day name.
            Default is English locale.

        Returns
        -------
        Series or Index
            Series or Index of day names.

        Examples
        --------
        >>> s = pd.Series(pd.date_range(start='2018-01-01', freq='D', periods=3))
        >>> s
        0   2018-01-01
        1   2018-01-02
        2   2018-01-03
        dtype: datetime64[ns]
        >>> s.dt.day_name()
        0       Monday
        1      Tuesday
        2    Wednesday
        dtype: object

        >>> idx = pd.date_range(start='2018-01-01', freq='D', periods=3)
        >>> idx
        DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03'],
                      dtype='datetime64[ns]', freq='D')
        >>> idx.day_name()
        Index(['Monday', 'Tuesday', 'Wednesday'], dtype='object')
        """
values = self._local_timestamps()

result = fields.get_date_name_field(
    values, "day_name", locale=locale, reso=self._creso
)
result = self._maybe_mask_results(result, fill_value=None)
exit(result)
