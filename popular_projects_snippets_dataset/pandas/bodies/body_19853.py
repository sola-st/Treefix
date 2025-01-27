# Extracted from ./data/repos/pandas/pandas/core/tools/timedeltas.py
"""
    Convert argument to timedelta.

    Timedeltas are absolute differences in times, expressed in difference
    units (e.g. days, hours, minutes, seconds). This method converts
    an argument from a recognized timedelta format / value into
    a Timedelta type.

    Parameters
    ----------
    arg : str, timedelta, list-like or Series
        The data to be converted to timedelta.

        .. versionchanged:: 2.0
            Strings with units 'M', 'Y' and 'y' do not represent
            unambiguous timedelta values and will raise an exception.

    unit : str, optional
        Denotes the unit of the arg for numeric `arg`. Defaults to ``"ns"``.

        Possible values:

        * 'W'
        * 'D' / 'days' / 'day'
        * 'hours' / 'hour' / 'hr' / 'h'
        * 'm' / 'minute' / 'min' / 'minutes' / 'T'
        * 'S' / 'seconds' / 'sec' / 'second'
        * 'ms' / 'milliseconds' / 'millisecond' / 'milli' / 'millis' / 'L'
        * 'us' / 'microseconds' / 'microsecond' / 'micro' / 'micros' / 'U'
        * 'ns' / 'nanoseconds' / 'nano' / 'nanos' / 'nanosecond' / 'N'

        .. versionchanged:: 1.1.0

           Must not be specified when `arg` context strings and
           ``errors="raise"``.

    errors : {'ignore', 'raise', 'coerce'}, default 'raise'
        - If 'raise', then invalid parsing will raise an exception.
        - If 'coerce', then invalid parsing will be set as NaT.
        - If 'ignore', then invalid parsing will return the input.

    Returns
    -------
    timedelta
        If parsing succeeded.
        Return type depends on input:

        - list-like: TimedeltaIndex of timedelta64 dtype
        - Series: Series of timedelta64 dtype
        - scalar: Timedelta

    See Also
    --------
    DataFrame.astype : Cast argument to a specified dtype.
    to_datetime : Convert argument to datetime.
    convert_dtypes : Convert dtypes.

    Notes
    -----
    If the precision is higher than nanoseconds, the precision of the duration is
    truncated to nanoseconds for string inputs.

    Examples
    --------
    Parsing a single string to a Timedelta:

    >>> pd.to_timedelta('1 days 06:05:01.00003')
    Timedelta('1 days 06:05:01.000030')
    >>> pd.to_timedelta('15.5us')
    Timedelta('0 days 00:00:00.000015500')

    Parsing a list or array of strings:

    >>> pd.to_timedelta(['1 days 06:05:01.00003', '15.5us', 'nan'])
    TimedeltaIndex(['1 days 06:05:01.000030', '0 days 00:00:00.000015500', NaT],
                   dtype='timedelta64[ns]', freq=None)

    Converting numbers by specifying the `unit` keyword argument:

    >>> pd.to_timedelta(np.arange(5), unit='s')
    TimedeltaIndex(['0 days 00:00:00', '0 days 00:00:01', '0 days 00:00:02',
                    '0 days 00:00:03', '0 days 00:00:04'],
                   dtype='timedelta64[ns]', freq=None)
    >>> pd.to_timedelta(np.arange(5), unit='d')
    TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'],
                   dtype='timedelta64[ns]', freq=None)
    """
if unit is not None:
    unit = parse_timedelta_unit(unit)

if errors not in ("ignore", "raise", "coerce"):
    raise ValueError("errors must be one of 'ignore', 'raise', or 'coerce'.")

if unit in {"Y", "y", "M"}:
    raise ValueError(
        "Units 'M', 'Y', and 'y' are no longer supported, as they do not "
        "represent unambiguous timedelta values durations."
    )

if arg is None:
    exit(arg)
elif isinstance(arg, ABCSeries):
    values = _convert_listlike(arg._values, unit=unit, errors=errors)
    exit(arg._constructor(values, index=arg.index, name=arg.name))
elif isinstance(arg, ABCIndex):
    exit(_convert_listlike(arg, unit=unit, errors=errors, name=arg.name))
elif isinstance(arg, np.ndarray) and arg.ndim == 0:
    # extract array scalar and process below
    # error: Incompatible types in assignment (expression has type "object",
    # variable has type "Union[str, int, float, timedelta, List[Any],
    # Tuple[Any, ...], Union[Union[ExtensionArray, ndarray[Any, Any]], Index,
    # Series]]")  [assignment]
    arg = lib.item_from_zerodim(arg)  # type: ignore[assignment]
elif is_list_like(arg) and getattr(arg, "ndim", 1) == 1:
    exit(_convert_listlike(arg, unit=unit, errors=errors))
elif getattr(arg, "ndim", 1) > 1:
    raise TypeError(
        "arg must be a string, timedelta, list, tuple, 1-d array, or Series"
    )

if isinstance(arg, str) and unit is not None:
    raise ValueError("unit must not be specified if the input is/contains a str")

# ...so it must be a scalar value. Return scalar.
exit(_coerce_scalar_to_timedelta_type(arg, unit=unit, errors=errors))
