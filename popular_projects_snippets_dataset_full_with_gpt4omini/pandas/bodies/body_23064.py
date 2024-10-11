# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Localize tz-naive index of a Series or DataFrame to target time zone.

        This operation localizes the Index. To localize the values in a
        timezone-naive Series, use :meth:`Series.dt.tz_localize`.

        Parameters
        ----------
        tz : str or tzinfo or None
            Time zone to localize. Passing ``None`` will remove the
            time zone information and preserve local time.
        axis : {{0 or 'index', 1 or 'columns'}}, default 0
            The axis to localize
        level : int, str, default None
            If axis ia a MultiIndex, localize a specific level. Otherwise
            must be None.
        copy : bool, default True
            Also make a copy of the underlying data.
        ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
            When clocks moved backward due to DST, ambiguous times may arise.
            For example in Central European Time (UTC+01), when going from
            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at
            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the
            `ambiguous` parameter dictates how ambiguous times should be
            handled.

            - 'infer' will attempt to infer fall dst-transition hours based on
              order
            - bool-ndarray where True signifies a DST time, False designates
              a non-DST time (note that this flag is only applicable for
              ambiguous times)
            - 'NaT' will return NaT where there are ambiguous times
            - 'raise' will raise an AmbiguousTimeError if there are ambiguous
              times.
        nonexistent : str, default 'raise'
            A nonexistent time does not exist in a particular timezone
            where clocks moved forward due to DST. Valid values are:

            - 'shift_forward' will shift the nonexistent time forward to the
              closest existing time
            - 'shift_backward' will shift the nonexistent time backward to the
              closest existing time
            - 'NaT' will return NaT where there are nonexistent times
            - timedelta objects will shift nonexistent times by the timedelta
            - 'raise' will raise an NonExistentTimeError if there are
              nonexistent times.

        Returns
        -------
        {klass}
            Same type as the input.

        Raises
        ------
        TypeError
            If the TimeSeries is tz-aware and tz is not None.

        Examples
        --------
        Localize local times:

        >>> s = pd.Series(
        ...     [1],
        ...     index=pd.DatetimeIndex(['2018-09-15 01:30:00']),
        ... )
        >>> s.tz_localize('CET')
        2018-09-15 01:30:00+02:00    1
        dtype: int64

        Pass None to convert to tz-naive index and preserve local time:

        >>> s = pd.Series([1],
        ...     index=pd.DatetimeIndex(['2018-09-15 01:30:00+02:00']))
        >>> s.tz_localize(None)
        2018-09-15 01:30:00    1
        dtype: int64

        Be careful with DST changes. When there is sequential data, pandas
        can infer the DST time:

        >>> s = pd.Series(range(7),
        ...               index=pd.DatetimeIndex(['2018-10-28 01:30:00',
        ...                                       '2018-10-28 02:00:00',
        ...                                       '2018-10-28 02:30:00',
        ...                                       '2018-10-28 02:00:00',
        ...                                       '2018-10-28 02:30:00',
        ...                                       '2018-10-28 03:00:00',
        ...                                       '2018-10-28 03:30:00']))
        >>> s.tz_localize('CET', ambiguous='infer')
        2018-10-28 01:30:00+02:00    0
        2018-10-28 02:00:00+02:00    1
        2018-10-28 02:30:00+02:00    2
        2018-10-28 02:00:00+01:00    3
        2018-10-28 02:30:00+01:00    4
        2018-10-28 03:00:00+01:00    5
        2018-10-28 03:30:00+01:00    6
        dtype: int64

        In some cases, inferring the DST is impossible. In such cases, you can
        pass an ndarray to the ambiguous parameter to set the DST explicitly

        >>> s = pd.Series(range(3),
        ...               index=pd.DatetimeIndex(['2018-10-28 01:20:00',
        ...                                       '2018-10-28 02:36:00',
        ...                                       '2018-10-28 03:46:00']))
        >>> s.tz_localize('CET', ambiguous=np.array([True, True, False]))
        2018-10-28 01:20:00+02:00    0
        2018-10-28 02:36:00+02:00    1
        2018-10-28 03:46:00+01:00    2
        dtype: int64

        If the DST transition causes nonexistent times, you can shift these
        dates forward or backward with a timedelta object or `'shift_forward'`
        or `'shift_backward'`.

        >>> s = pd.Series(range(2),
        ...               index=pd.DatetimeIndex(['2015-03-29 02:30:00',
        ...                                       '2015-03-29 03:30:00']))
        >>> s.tz_localize('Europe/Warsaw', nonexistent='shift_forward')
        2015-03-29 03:00:00+02:00    0
        2015-03-29 03:30:00+02:00    1
        dtype: int64
        >>> s.tz_localize('Europe/Warsaw', nonexistent='shift_backward')
        2015-03-29 01:59:59.999999999+01:00    0
        2015-03-29 03:30:00+02:00              1
        dtype: int64
        >>> s.tz_localize('Europe/Warsaw', nonexistent=pd.Timedelta('1H'))
        2015-03-29 03:30:00+02:00    0
        2015-03-29 03:30:00+02:00    1
        dtype: int64
        """
nonexistent_options = ("raise", "NaT", "shift_forward", "shift_backward")
if nonexistent not in nonexistent_options and not isinstance(
    nonexistent, dt.timedelta
):
    raise ValueError(
        "The nonexistent argument must be one of 'raise', "
        "'NaT', 'shift_forward', 'shift_backward' or "
        "a timedelta object"
    )

axis = self._get_axis_number(axis)
ax = self._get_axis(axis)

def _tz_localize(ax, tz, ambiguous, nonexistent):
    if not hasattr(ax, "tz_localize"):
        if len(ax) > 0:
            ax_name = self._get_axis_name(axis)
            raise TypeError(
                f"{ax_name} is not a valid DatetimeIndex or PeriodIndex"
            )
        ax = DatetimeIndex([], tz=tz)
    else:
        ax = ax.tz_localize(tz, ambiguous=ambiguous, nonexistent=nonexistent)
    exit(ax)

# if a level is given it must be a MultiIndex level or
# equivalent to the axis name
if isinstance(ax, MultiIndex):
    level = ax._get_level_number(level)
    new_level = _tz_localize(ax.levels[level], tz, ambiguous, nonexistent)
    ax = ax.set_levels(new_level, level=level)
else:
    if level not in (None, 0, ax.name):
        raise ValueError(f"The level {level} is not valid")
    ax = _tz_localize(ax, tz, ambiguous, nonexistent)

result = self.copy(deep=copy)
result = result.set_axis(ax, axis=axis, copy=False)
exit(result.__finalize__(self, method="tz_localize"))
