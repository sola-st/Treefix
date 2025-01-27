# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Cast to PeriodArray/Index at a particular frequency.

        Converts DatetimeArray/Index to PeriodArray/Index.

        Parameters
        ----------
        freq : str or Offset, optional
            One of pandas' :ref:`offset strings <timeseries.offset_aliases>`
            or an Offset object. Will be inferred by default.

        Returns
        -------
        PeriodArray/Index

        Raises
        ------
        ValueError
            When converting a DatetimeArray/Index with non-regular values,
            so that a frequency cannot be inferred.

        See Also
        --------
        PeriodIndex: Immutable ndarray holding ordinal values.
        DatetimeIndex.to_pydatetime: Return DatetimeIndex as object.

        Examples
        --------
        >>> df = pd.DataFrame({"y": [1, 2, 3]},
        ...                   index=pd.to_datetime(["2000-03-31 00:00:00",
        ...                                         "2000-05-31 00:00:00",
        ...                                         "2000-08-31 00:00:00"]))
        >>> df.index.to_period("M")
        PeriodIndex(['2000-03', '2000-05', '2000-08'],
                    dtype='period[M]')

        Infer the daily frequency

        >>> idx = pd.date_range("2017-01-01", periods=2)
        >>> idx.to_period()
        PeriodIndex(['2017-01-01', '2017-01-02'],
                    dtype='period[D]')
        """
from pandas.core.arrays import PeriodArray

if self.tz is not None:
    warnings.warn(
        "Converting to PeriodArray/Index representation "
        "will drop timezone information.",
        UserWarning,
        stacklevel=find_stack_level(),
    )

if freq is None:
    freq = self.freqstr or self.inferred_freq

    if freq is None:
        raise ValueError(
            "You must pass a freq argument as current index has none."
        )

    res = get_period_alias(freq)

    #  https://github.com/pandas-dev/pandas/issues/33358
    if res is None:
        res = freq

    freq = res

exit(PeriodArray._from_datetime64(self._ndarray, freq, tz=self.tz))
