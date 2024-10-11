# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Provide resampling when using a TimeGrouper.

        Given a grouper, the function resamples it according to a string
        "string" -> "frequency".

        See the :ref:`frequency aliases <timeseries.offset_aliases>`
        documentation for more details.

        Parameters
        ----------
        rule : str or DateOffset
            The offset string or object representing target grouper conversion.
        *args, **kwargs
            Possible arguments are `how`, `fill_method`, `limit`, `kind` and
            `on`, and other arguments of `TimeGrouper`.

        Returns
        -------
        Grouper
            Return a new grouper with our resampler appended.

        See Also
        --------
        Grouper : Specify a frequency to resample with when
            grouping by a key.
        DatetimeIndex.resample : Frequency conversion and resampling of
            time series.

        Examples
        --------
        >>> idx = pd.date_range('1/1/2000', periods=4, freq='T')
        >>> df = pd.DataFrame(data=4 * [range(2)],
        ...                   index=idx,
        ...                   columns=['a', 'b'])
        >>> df.iloc[2, 0] = 5
        >>> df
                            a  b
        2000-01-01 00:00:00  0  1
        2000-01-01 00:01:00  0  1
        2000-01-01 00:02:00  5  1
        2000-01-01 00:03:00  0  1

        Downsample the DataFrame into 3 minute bins and sum the values of
        the timestamps falling into a bin.

        >>> df.groupby('a').resample('3T').sum()
                                 a  b
        a
        0   2000-01-01 00:00:00  0  2
            2000-01-01 00:03:00  0  1
        5   2000-01-01 00:00:00  5  1

        Upsample the series into 30 second bins.

        >>> df.groupby('a').resample('30S').sum()
                            a  b
        a
        0   2000-01-01 00:00:00  0  1
            2000-01-01 00:00:30  0  0
            2000-01-01 00:01:00  0  1
            2000-01-01 00:01:30  0  0
            2000-01-01 00:02:00  0  0
            2000-01-01 00:02:30  0  0
            2000-01-01 00:03:00  0  1
        5   2000-01-01 00:02:00  5  1

        Resample by month. Values are assigned to the month of the period.

        >>> df.groupby('a').resample('M').sum()
                    a  b
        a
        0   2000-01-31  0  3
        5   2000-01-31  5  1

        Downsample the series into 3 minute bins as above, but close the right
        side of the bin interval.

        >>> df.groupby('a').resample('3T', closed='right').sum()
                                 a  b
        a
        0   1999-12-31 23:57:00  0  1
            2000-01-01 00:00:00  0  2
        5   2000-01-01 00:00:00  5  1

        Downsample the series into 3 minute bins and close the right side of
        the bin interval, but label each bin using the right edge instead of
        the left.

        >>> df.groupby('a').resample('3T', closed='right', label='right').sum()
                                 a  b
        a
        0   2000-01-01 00:00:00  0  1
            2000-01-01 00:03:00  0  2
        5   2000-01-01 00:03:00  5  1
        """
from pandas.core.resample import get_resampler_for_grouping

exit(get_resampler_for_grouping(self, rule, *args, **kwargs))
