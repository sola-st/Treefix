# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
    Return a fixed frequency IntervalIndex.

    Parameters
    ----------
    start : numeric or datetime-like, default None
        Left bound for generating intervals.
    end : numeric or datetime-like, default None
        Right bound for generating intervals.
    periods : int, default None
        Number of periods to generate.
    freq : numeric, str, datetime.timedelta, or DateOffset, default None
        The length of each interval. Must be consistent with the type of start
        and end, e.g. 2 for numeric, or '5H' for datetime-like.  Default is 1
        for numeric and 'D' for datetime-like.
    name : str, default None
        Name of the resulting IntervalIndex.
    closed : {'left', 'right', 'both', 'neither'}, default 'right'
        Whether the intervals are closed on the left-side, right-side, both
        or neither.

    Returns
    -------
    IntervalIndex

    See Also
    --------
    IntervalIndex : An Index of intervals that are all closed on the same side.

    Notes
    -----
    Of the four parameters ``start``, ``end``, ``periods``, and ``freq``,
    exactly three must be specified. If ``freq`` is omitted, the resulting
    ``IntervalIndex`` will have ``periods`` linearly spaced elements between
    ``start`` and ``end``, inclusively.

    To learn more about datetime-like frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.

    Examples
    --------
    Numeric ``start`` and  ``end`` is supported.

    >>> pd.interval_range(start=0, end=5)
    IntervalIndex([(0, 1], (1, 2], (2, 3], (3, 4], (4, 5]],
                  dtype='interval[int64, right]')

    Additionally, datetime-like input is also supported.

    >>> pd.interval_range(start=pd.Timestamp('2017-01-01'),
    ...                   end=pd.Timestamp('2017-01-04'))
    IntervalIndex([(2017-01-01, 2017-01-02], (2017-01-02, 2017-01-03],
                   (2017-01-03, 2017-01-04]],
                  dtype='interval[datetime64[ns], right]')

    The ``freq`` parameter specifies the frequency between the left and right.
    endpoints of the individual intervals within the ``IntervalIndex``.  For
    numeric ``start`` and ``end``, the frequency must also be numeric.

    >>> pd.interval_range(start=0, periods=4, freq=1.5)
    IntervalIndex([(0.0, 1.5], (1.5, 3.0], (3.0, 4.5], (4.5, 6.0]],
                  dtype='interval[float64, right]')

    Similarly, for datetime-like ``start`` and ``end``, the frequency must be
    convertible to a DateOffset.

    >>> pd.interval_range(start=pd.Timestamp('2017-01-01'),
    ...                   periods=3, freq='MS')
    IntervalIndex([(2017-01-01, 2017-02-01], (2017-02-01, 2017-03-01],
                   (2017-03-01, 2017-04-01]],
                  dtype='interval[datetime64[ns], right]')

    Specify ``start``, ``end``, and ``periods``; the frequency is generated
    automatically (linearly spaced).

    >>> pd.interval_range(start=0, end=6, periods=4)
    IntervalIndex([(0.0, 1.5], (1.5, 3.0], (3.0, 4.5], (4.5, 6.0]],
              dtype='interval[float64, right]')

    The ``closed`` parameter specifies which endpoints of the individual
    intervals within the ``IntervalIndex`` are closed.

    >>> pd.interval_range(end=5, periods=4, closed='both')
    IntervalIndex([[1, 2], [2, 3], [3, 4], [4, 5]],
                  dtype='interval[int64, both]')
    """
start = maybe_box_datetimelike(start)
end = maybe_box_datetimelike(end)
endpoint = start if start is not None else end

if freq is None and com.any_none(periods, start, end):
    freq = 1 if is_number(endpoint) else "D"

if com.count_not_none(start, end, periods, freq) != 3:
    raise ValueError(
        "Of the four parameters: start, end, periods, and "
        "freq, exactly three must be specified"
    )

if not _is_valid_endpoint(start):
    raise ValueError(f"start must be numeric or datetime-like, got {start}")
if not _is_valid_endpoint(end):
    raise ValueError(f"end must be numeric or datetime-like, got {end}")

if is_float(periods):
    periods = int(periods)
elif not is_integer(periods) and periods is not None:
    raise TypeError(f"periods must be a number, got {periods}")

if freq is not None and not is_number(freq):
    try:
        freq = to_offset(freq)
    except ValueError as err:
        raise ValueError(
            f"freq must be numeric or convertible to DateOffset, got {freq}"
        ) from err

    # verify type compatibility
if not all(
    [
        _is_type_compatible(start, end),
        _is_type_compatible(start, freq),
        _is_type_compatible(end, freq),
    ]
):
    raise TypeError("start, end, freq need to be type compatible")

# +1 to convert interval count to breaks count (n breaks = n-1 intervals)
if periods is not None:
    periods += 1

breaks: np.ndarray | TimedeltaIndex | DatetimeIndex

if is_number(endpoint):
    # force consistency between start/end/freq (lower end if freq skips it)
    if com.all_not_none(start, end, freq):
        end -= (end - start) % freq

    # compute the period/start/end if unspecified (at most one)
    if periods is None:
        periods = int((end - start) // freq) + 1
    elif start is None:
        start = end - (periods - 1) * freq
    elif end is None:
        end = start + (periods - 1) * freq

    breaks = np.linspace(start, end, periods)
    if all(is_integer(x) for x in com.not_none(start, end, freq)):
        # np.linspace always produces float output

        # error: Argument 1 to "maybe_downcast_numeric" has incompatible type
        # "Union[ndarray[Any, Any], TimedeltaIndex, DatetimeIndex]";
        # expected "ndarray[Any, Any]"  [
        breaks = maybe_downcast_numeric(
            breaks,  # type: ignore[arg-type]
            np.dtype("int64"),
        )
else:
    # delegate to the appropriate range function
    if isinstance(endpoint, Timestamp):
        breaks = date_range(start=start, end=end, periods=periods, freq=freq)
    else:
        breaks = timedelta_range(start=start, end=end, periods=periods, freq=freq)

exit(IntervalIndex.from_breaks(breaks, name=name, closed=closed))
