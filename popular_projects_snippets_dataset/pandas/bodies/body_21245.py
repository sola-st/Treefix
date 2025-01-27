# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
"""
    Parameters
    ----------
    data : list-like
    copy : bool, default False
    unit : str, optional
        The timedelta unit to treat integers as multiples of. For numeric
        data this defaults to ``'ns'``.
        Must be un-specified if the data contains a str and ``errors=="raise"``.
    errors : {"raise", "coerce", "ignore"}, default "raise"
        How to handle elements that cannot be converted to timedelta64[ns].
        See ``pandas.to_timedelta`` for details.

    Returns
    -------
    converted : numpy.ndarray
        The sequence converted to a numpy array with dtype ``timedelta64[ns]``.
    inferred_freq : Tick or None
        The inferred frequency of the sequence.

    Raises
    ------
    ValueError : Data cannot be converted to timedelta64[ns].

    Notes
    -----
    Unlike `pandas.to_timedelta`, if setting ``errors=ignore`` will not cause
    errors to be ignored; they are caught and subsequently ignored at a
    higher level.
    """
assert unit not in ["Y", "y", "M"]  # caller is responsible for checking

inferred_freq = None
if unit is not None:
    unit = parse_timedelta_unit(unit)

data, copy = dtl.ensure_arraylike_for_datetimelike(
    data, copy, cls_name="TimedeltaArray"
)

if isinstance(data, TimedeltaArray):
    inferred_freq = data.freq

# Convert whatever we have into timedelta64[ns] dtype
if is_object_dtype(data.dtype) or is_string_dtype(data.dtype):
    # no need to make a copy, need to convert if string-dtyped
    data = _objects_to_td64ns(data, unit=unit, errors=errors)
    copy = False

elif is_integer_dtype(data.dtype):
    # treat as multiples of the given unit
    data, copy_made = _ints_to_td64ns(data, unit=unit)
    copy = copy and not copy_made

elif is_float_dtype(data.dtype):
    # cast the unit, multiply base/frac separately
    # to avoid precision issues from float -> int
    if is_extension_array_dtype(data):
        mask = data._mask
        data = data._data
    else:
        mask = np.isnan(data)
    # The next few lines are effectively a vectorized 'cast_from_unit'
    m, p = precision_from_unit(unit or "ns")
    base = data.astype(np.int64)
    frac = data - base
    if p:
        frac = np.round(frac, p)
    data = (base * m + (frac * m).astype(np.int64)).view("timedelta64[ns]")
    data[mask] = iNaT
    copy = False

elif is_timedelta64_dtype(data.dtype):
    data_unit = get_unit_from_dtype(data.dtype)
    if not is_supported_unit(data_unit):
        # cast to closest supported unit, i.e. s or ns
        new_reso = get_supported_reso(data_unit)
        new_unit = npy_unit_to_abbrev(new_reso)
        new_dtype = np.dtype(f"m8[{new_unit}]")
        data = astype_overflowsafe(data, dtype=new_dtype, copy=False)
        copy = False

else:
    # This includes datetime64-dtype, see GH#23539, GH#29794
    raise TypeError(f"dtype {data.dtype} cannot be converted to timedelta64[ns]")

data = np.array(data, copy=copy)

assert data.dtype.kind == "m"
assert data.dtype != "m8"  # i.e. not unit-less

exit((data, inferred_freq))
