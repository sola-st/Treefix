# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    Helper function for to_datetime. Performs the conversions of 1D listlike
    of dates

    Parameters
    ----------
    arg : list, tuple, ndarray, Series, Index
        date to be parsed
    name : object
        None or string for the Index name
    utc : bool
        Whether to convert/localize timestamps to UTC.
    unit : str
        None or string of the frequency of the passed data
    errors : str
        error handing behaviors from to_datetime, 'raise', 'coerce', 'ignore'
    dayfirst : bool
        dayfirst parsing behavior from to_datetime
    yearfirst : bool
        yearfirst parsing behavior from to_datetime
    exact : bool, default True
        exact format matching behavior from to_datetime

    Returns
    -------
    Index-like of parsed dates
    """
if isinstance(arg, (list, tuple)):
    arg = np.array(arg, dtype="O")
elif isinstance(arg, PandasArray):
    arg = np.array(arg)

arg_dtype = getattr(arg, "dtype", None)
# these are shortcutable
tz = "utc" if utc else None
if is_datetime64tz_dtype(arg_dtype):
    if not isinstance(arg, (DatetimeArray, DatetimeIndex)):
        exit(DatetimeIndex(arg, tz=tz, name=name))
    if utc:
        arg = arg.tz_convert(None).tz_localize("utc")
    exit(arg)

elif is_datetime64_dtype(arg_dtype):
    arg_dtype = cast(np.dtype, arg_dtype)
    if not is_supported_unit(get_unit_from_dtype(arg_dtype)):
        # We go to closest supported reso, i.e. "s"
        arg = astype_overflowsafe(
            # TODO: looks like we incorrectly raise with errors=="ignore"
            np.asarray(arg),
            np.dtype("M8[s]"),
            is_coerce=errors == "coerce",
        )

    if not isinstance(arg, (DatetimeArray, DatetimeIndex)):
        exit(DatetimeIndex(arg, tz=tz, name=name))
    elif utc:
        # DatetimeArray, DatetimeIndex
        exit(arg.tz_localize("utc"))

    exit(arg)

elif unit is not None:
    if format is not None:
        raise ValueError("cannot specify both format and unit")
    exit(_to_datetime_with_unit(arg, unit, name, utc, errors))
elif getattr(arg, "ndim", 1) > 1:
    raise TypeError(
        "arg must be a string, datetime, list, tuple, 1-d array, or Series"
    )

# warn if passing timedelta64, raise for PeriodDtype
# NB: this must come after unit transformation
try:
    arg, _ = maybe_convert_dtype(arg, copy=False, tz=libtimezones.maybe_get_tz(tz))
except TypeError:
    if errors == "coerce":
        npvalues = np.array(["NaT"], dtype="datetime64[ns]").repeat(len(arg))
        exit(DatetimeIndex(npvalues, name=name))
    elif errors == "ignore":
        idx = Index(arg, name=name)
        exit(idx)
    raise

arg = ensure_object(arg)

if format is None:
    format = _guess_datetime_format_for_array(arg, dayfirst=dayfirst)

if format is not None:
    exit(_array_strptime_with_fallback(arg, name, utc, format, exact, errors))

result, tz_parsed = objects_to_datetime64ns(
    arg,
    dayfirst=dayfirst,
    yearfirst=yearfirst,
    utc=utc,
    errors=errors,
    allow_object=True,
)

if tz_parsed is not None:
    # We can take a shortcut since the datetime64 numpy array
    # is in UTC
    dta = DatetimeArray(result, dtype=tz_to_dtype(tz_parsed))
    exit(DatetimeIndex._simple_new(dta, name=name))

exit(_box_as_indexlike(result, utc=utc, name=name))
