# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
"""
    Return a fixed frequency DatetimeIndex with business day as the default.

    Parameters
    ----------
    start : str or datetime-like, default None
        Left bound for generating dates.
    end : str or datetime-like, default None
        Right bound for generating dates.
    periods : int, default None
        Number of periods to generate.
    freq : str, Timedelta, datetime.timedelta, or DateOffset, default 'B'
        Frequency strings can have multiples, e.g. '5H'. The default is
        business daily ('B').
    tz : str or None
        Time zone name for returning localized DatetimeIndex, for example
        Asia/Beijing.
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range.
    name : str, default None
        Name of the resulting DatetimeIndex.
    weekmask : str or None, default None
        Weekmask of valid business days, passed to ``numpy.busdaycalendar``,
        only used when custom frequency strings are passed.  The default
        value None is equivalent to 'Mon Tue Wed Thu Fri'.
    holidays : list-like or None, default None
        Dates to exclude from the set of valid business days, passed to
        ``numpy.busdaycalendar``, only used when custom frequency strings
        are passed.
    inclusive : {"both", "neither", "left", "right"}, default "both"
        Include boundaries; Whether to set each bound as closed or open.

        .. versionadded:: 1.4.0
    **kwargs
        For compatibility. Has no effect on the result.

    Returns
    -------
    DatetimeIndex

    Notes
    -----
    Of the four parameters: ``start``, ``end``, ``periods``, and ``freq``,
    exactly three must be specified.  Specifying ``freq`` is a requirement
    for ``bdate_range``.  Use ``date_range`` if specifying ``freq`` is not
    desired.

    To learn more about the frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.

    Examples
    --------
    Note how the two weekend days are skipped in the result.

    >>> pd.bdate_range(start='1/1/2018', end='1/08/2018')
    DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
               '2018-01-05', '2018-01-08'],
              dtype='datetime64[ns]', freq='B')
    """
if freq is None:
    msg = "freq must be specified for bdate_range; use date_range instead"
    raise TypeError(msg)

if isinstance(freq, str) and freq.startswith("C"):
    try:
        weekmask = weekmask or "Mon Tue Wed Thu Fri"
        freq = prefix_mapping[freq](holidays=holidays, weekmask=weekmask)
    except (KeyError, TypeError) as err:
        msg = f"invalid custom frequency string: {freq}"
        raise ValueError(msg) from err
elif holidays or weekmask:
    msg = (
        "a custom frequency string is required when holidays or "
        f"weekmask are passed, got frequency {freq}"
    )
    raise ValueError(msg)

exit(date_range(
    start=start,
    end=end,
    periods=periods,
    freq=freq,
    tz=tz,
    normalize=normalize,
    name=name,
    inclusive=inclusive,
    **kwargs,
))
