# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Resample time-series data.

        Convenience method for frequency conversion and resampling of time series.
        The object must have a datetime-like index (`DatetimeIndex`, `PeriodIndex`,
        or `TimedeltaIndex`), or the caller must pass the label of a datetime-like
        series/index to the ``on``/``level`` keyword parameter.

        Parameters
        ----------
        rule : DateOffset, Timedelta or str
            The offset string or object representing target conversion.
        axis : {{0 or 'index', 1 or 'columns'}}, default 0
            Which axis to use for up- or down-sampling. For `Series` this parameter
            is unused and defaults to 0. Must be
            `DatetimeIndex`, `TimedeltaIndex` or `PeriodIndex`.
        closed : {{'right', 'left'}}, default None
            Which side of bin interval is closed. The default is 'left'
            for all frequency offsets except for 'M', 'A', 'Q', 'BM',
            'BA', 'BQ', and 'W' which all have a default of 'right'.
        label : {{'right', 'left'}}, default None
            Which bin edge label to label bucket with. The default is 'left'
            for all frequency offsets except for 'M', 'A', 'Q', 'BM',
            'BA', 'BQ', and 'W' which all have a default of 'right'.
        convention : {{'start', 'end', 's', 'e'}}, default 'start'
            For `PeriodIndex` only, controls whether to use the start or
            end of `rule`.
        kind : {{'timestamp', 'period'}}, optional, default None
            Pass 'timestamp' to convert the resulting index to a
            `DateTimeIndex` or 'period' to convert it to a `PeriodIndex`.
            By default the input representation is retained.

        on : str, optional
            For a DataFrame, column to use instead of index for resampling.
            Column must be datetime-like.
        level : str or int, optional
            For a MultiIndex, level (name or number) to use for
            resampling. `level` must be datetime-like.
        origin : Timestamp or str, default 'start_day'
            The timestamp on which to adjust the grouping. The timezone of origin
            must match the timezone of the index.
            If string, must be one of the following:

            - 'epoch': `origin` is 1970-01-01
            - 'start': `origin` is the first value of the timeseries
            - 'start_day': `origin` is the first day at midnight of the timeseries

            .. versionadded:: 1.1.0

            - 'end': `origin` is the last value of the timeseries
            - 'end_day': `origin` is the ceiling midnight of the last day

            .. versionadded:: 1.3.0

        offset : Timedelta or str, default is None
            An offset timedelta added to the origin.

            .. versionadded:: 1.1.0

        group_keys : bool, optional
            Whether to include the group keys in the result index when using
            ``.apply()`` on the resampled object. Not specifying ``group_keys``
            will retain values-dependent behavior from pandas 1.4
            and earlier (see :ref:`pandas 1.5.0 Release notes
            <whatsnew_150.enhancements.resample_group_keys>`
            for examples). In a future version of pandas, the behavior will
            default to the same as specifying ``group_keys=False``.

            .. versionadded:: 1.5.0

        Returns
        -------
        pandas.core.Resampler
            :class:`~pandas.core.Resampler` object.

        See Also
        --------
        Series.resample : Resample a Series.
        DataFrame.resample : Resample a DataFrame.
        groupby : Group {klass} by mapping, function, label, or list of labels.
        asfreq : Reindex a {klass} with the given frequency without grouping.

        Notes
        -----
        See the `user guide
        <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#resampling>`__
        for more.

        To learn more about the offset strings, please see `this link
        <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects>`__.

        Examples
        --------
        Start by creating a series with 9 one minute timestamps.

        >>> index = pd.date_range('1/1/2000', periods=9, freq='T')
        >>> series = pd.Series(range(9), index=index)
        >>> series
        2000-01-01 00:00:00    0
        2000-01-01 00:01:00    1
        2000-01-01 00:02:00    2
        2000-01-01 00:03:00    3
        2000-01-01 00:04:00    4
        2000-01-01 00:05:00    5
        2000-01-01 00:06:00    6
        2000-01-01 00:07:00    7
        2000-01-01 00:08:00    8
        Freq: T, dtype: int64

        Downsample the series into 3 minute bins and sum the values
        of the timestamps falling into a bin.

        >>> series.resample('3T').sum()
        2000-01-01 00:00:00     3
        2000-01-01 00:03:00    12
        2000-01-01 00:06:00    21
        Freq: 3T, dtype: int64

        Downsample the series into 3 minute bins as above, but label each
        bin using the right edge instead of the left. Please note that the
        value in the bucket used as the label is not included in the bucket,
        which it labels. For example, in the original series the
        bucket ``2000-01-01 00:03:00`` contains the value 3, but the summed
        value in the resampled bucket with the label ``2000-01-01 00:03:00``
        does not include 3 (if it did, the summed value would be 6, not 3).
        To include this value close the right side of the bin interval as
        illustrated in the example below this one.

        >>> series.resample('3T', label='right').sum()
        2000-01-01 00:03:00     3
        2000-01-01 00:06:00    12
        2000-01-01 00:09:00    21
        Freq: 3T, dtype: int64

        Downsample the series into 3 minute bins as above, but close the right
        side of the bin interval.

        >>> series.resample('3T', label='right', closed='right').sum()
        2000-01-01 00:00:00     0
        2000-01-01 00:03:00     6
        2000-01-01 00:06:00    15
        2000-01-01 00:09:00    15
        Freq: 3T, dtype: int64

        Upsample the series into 30 second bins.

        >>> series.resample('30S').asfreq()[0:5]   # Select first 5 rows
        2000-01-01 00:00:00   0.0
        2000-01-01 00:00:30   NaN
        2000-01-01 00:01:00   1.0
        2000-01-01 00:01:30   NaN
        2000-01-01 00:02:00   2.0
        Freq: 30S, dtype: float64

        Upsample the series into 30 second bins and fill the ``NaN``
        values using the ``ffill`` method.

        >>> series.resample('30S').ffill()[0:5]
        2000-01-01 00:00:00    0
        2000-01-01 00:00:30    0
        2000-01-01 00:01:00    1
        2000-01-01 00:01:30    1
        2000-01-01 00:02:00    2
        Freq: 30S, dtype: int64

        Upsample the series into 30 second bins and fill the
        ``NaN`` values using the ``bfill`` method.

        >>> series.resample('30S').bfill()[0:5]
        2000-01-01 00:00:00    0
        2000-01-01 00:00:30    1
        2000-01-01 00:01:00    1
        2000-01-01 00:01:30    2
        2000-01-01 00:02:00    2
        Freq: 30S, dtype: int64

        Pass a custom function via ``apply``

        >>> def custom_resampler(arraylike):
        ...     return np.sum(arraylike) + 5
        ...
        >>> series.resample('3T').apply(custom_resampler)
        2000-01-01 00:00:00     8
        2000-01-01 00:03:00    17
        2000-01-01 00:06:00    26
        Freq: 3T, dtype: int64

        For a Series with a PeriodIndex, the keyword `convention` can be
        used to control whether to use the start or end of `rule`.

        Resample a year by quarter using 'start' `convention`. Values are
        assigned to the first quarter of the period.

        >>> s = pd.Series([1, 2], index=pd.period_range('2012-01-01',
        ...                                             freq='A',
        ...                                             periods=2))
        >>> s
        2012    1
        2013    2
        Freq: A-DEC, dtype: int64
        >>> s.resample('Q', convention='start').asfreq()
        2012Q1    1.0
        2012Q2    NaN
        2012Q3    NaN
        2012Q4    NaN
        2013Q1    2.0
        2013Q2    NaN
        2013Q3    NaN
        2013Q4    NaN
        Freq: Q-DEC, dtype: float64

        Resample quarters by month using 'end' `convention`. Values are
        assigned to the last month of the period.

        >>> q = pd.Series([1, 2, 3, 4], index=pd.period_range('2018-01-01',
        ...                                                   freq='Q',
        ...                                                   periods=4))
        >>> q
        2018Q1    1
        2018Q2    2
        2018Q3    3
        2018Q4    4
        Freq: Q-DEC, dtype: int64
        >>> q.resample('M', convention='end').asfreq()
        2018-03    1.0
        2018-04    NaN
        2018-05    NaN
        2018-06    2.0
        2018-07    NaN
        2018-08    NaN
        2018-09    3.0
        2018-10    NaN
        2018-11    NaN
        2018-12    4.0
        Freq: M, dtype: float64

        For DataFrame objects, the keyword `on` can be used to specify the
        column instead of the index for resampling.

        >>> d = {{'price': [10, 11, 9, 13, 14, 18, 17, 19],
        ...      'volume': [50, 60, 40, 100, 50, 100, 40, 50]}}
        >>> df = pd.DataFrame(d)
        >>> df['week_starting'] = pd.date_range('01/01/2018',
        ...                                     periods=8,
        ...                                     freq='W')
        >>> df
           price  volume week_starting
        0     10      50    2018-01-07
        1     11      60    2018-01-14
        2      9      40    2018-01-21
        3     13     100    2018-01-28
        4     14      50    2018-02-04
        5     18     100    2018-02-11
        6     17      40    2018-02-18
        7     19      50    2018-02-25
        >>> df.resample('M', on='week_starting').mean()
                       price  volume
        week_starting
        2018-01-31     10.75    62.5
        2018-02-28     17.00    60.0

        For a DataFrame with MultiIndex, the keyword `level` can be used to
        specify on which level the resampling needs to take place.

        >>> days = pd.date_range('1/1/2000', periods=4, freq='D')
        >>> d2 = {{'price': [10, 11, 9, 13, 14, 18, 17, 19],
        ...       'volume': [50, 60, 40, 100, 50, 100, 40, 50]}}
        >>> df2 = pd.DataFrame(
        ...     d2,
        ...     index=pd.MultiIndex.from_product(
        ...         [days, ['morning', 'afternoon']]
        ...     )
        ... )
        >>> df2
                              price  volume
        2000-01-01 morning       10      50
                   afternoon     11      60
        2000-01-02 morning        9      40
                   afternoon     13     100
        2000-01-03 morning       14      50
                   afternoon     18     100
        2000-01-04 morning       17      40
                   afternoon     19      50
        >>> df2.resample('D', level=0).sum()
                    price  volume
        2000-01-01     21     110
        2000-01-02     22     140
        2000-01-03     32     150
        2000-01-04     36      90

        If you want to adjust the start of the bins based on a fixed timestamp:

        >>> start, end = '2000-10-01 23:30:00', '2000-10-02 00:30:00'
        >>> rng = pd.date_range(start, end, freq='7min')
        >>> ts = pd.Series(np.arange(len(rng)) * 3, index=rng)
        >>> ts
        2000-10-01 23:30:00     0
        2000-10-01 23:37:00     3
        2000-10-01 23:44:00     6
        2000-10-01 23:51:00     9
        2000-10-01 23:58:00    12
        2000-10-02 00:05:00    15
        2000-10-02 00:12:00    18
        2000-10-02 00:19:00    21
        2000-10-02 00:26:00    24
        Freq: 7T, dtype: int64

        >>> ts.resample('17min').sum()
        2000-10-01 23:14:00     0
        2000-10-01 23:31:00     9
        2000-10-01 23:48:00    21
        2000-10-02 00:05:00    54
        2000-10-02 00:22:00    24
        Freq: 17T, dtype: int64

        >>> ts.resample('17min', origin='epoch').sum()
        2000-10-01 23:18:00     0
        2000-10-01 23:35:00    18
        2000-10-01 23:52:00    27
        2000-10-02 00:09:00    39
        2000-10-02 00:26:00    24
        Freq: 17T, dtype: int64

        >>> ts.resample('17min', origin='2000-01-01').sum()
        2000-10-01 23:24:00     3
        2000-10-01 23:41:00    15
        2000-10-01 23:58:00    45
        2000-10-02 00:15:00    45
        Freq: 17T, dtype: int64

        If you want to adjust the start of the bins with an `offset` Timedelta, the two
        following lines are equivalent:

        >>> ts.resample('17min', origin='start').sum()
        2000-10-01 23:30:00     9
        2000-10-01 23:47:00    21
        2000-10-02 00:04:00    54
        2000-10-02 00:21:00    24
        Freq: 17T, dtype: int64

        >>> ts.resample('17min', offset='23h30min').sum()
        2000-10-01 23:30:00     9
        2000-10-01 23:47:00    21
        2000-10-02 00:04:00    54
        2000-10-02 00:21:00    24
        Freq: 17T, dtype: int64

        If you want to take the largest Timestamp as the end of the bins:

        >>> ts.resample('17min', origin='end').sum()
        2000-10-01 23:35:00     0
        2000-10-01 23:52:00    18
        2000-10-02 00:09:00    27
        2000-10-02 00:26:00    63
        Freq: 17T, dtype: int64

        In contrast with the `start_day`, you can use `end_day` to take the ceiling
        midnight of the largest Timestamp as the end of the bins and drop the bins
        not containing data:

        >>> ts.resample('17min', origin='end_day').sum()
        2000-10-01 23:38:00     3
        2000-10-01 23:55:00    15
        2000-10-02 00:12:00    45
        2000-10-02 00:29:00    45
        Freq: 17T, dtype: int64
        """
from pandas.core.resample import get_resampler

axis = self._get_axis_number(axis)
exit(get_resampler(
    self,
    freq=rule,
    label=label,
    closed=closed,
    axis=axis,
    kind=kind,
    convention=convention,
    key=on,
    level=level,
    origin=origin,
    offset=offset,
    group_keys=group_keys,
))
