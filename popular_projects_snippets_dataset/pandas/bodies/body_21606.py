# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
    Construct a new PeriodArray from a sequence of Period scalars.

    Parameters
    ----------
    data : Sequence of Period objects
        A sequence of Period objects. These are required to all have
        the same ``freq.`` Missing values can be indicated by ``None``
        or ``pandas.NaT``.
    freq : str, Tick, or Offset
        The frequency of every element of the array. This can be specified
        to avoid inferring the `freq` from `data`.
    copy : bool, default False
        Whether to ensure a copy of the data is made.

    Returns
    -------
    PeriodArray

    See Also
    --------
    PeriodArray
    pandas.PeriodIndex

    Examples
    --------
    >>> period_array([pd.Period('2017', freq='A'),
    ...               pd.Period('2018', freq='A')])
    <PeriodArray>
    ['2017', '2018']
    Length: 2, dtype: period[A-DEC]

    >>> period_array([pd.Period('2017', freq='A'),
    ...               pd.Period('2018', freq='A'),
    ...               pd.NaT])
    <PeriodArray>
    ['2017', '2018', 'NaT']
    Length: 3, dtype: period[A-DEC]

    Integers that look like years are handled

    >>> period_array([2000, 2001, 2002], freq='D')
    <PeriodArray>
    ['2000-01-01', '2001-01-01', '2002-01-01']
    Length: 3, dtype: period[D]

    Datetime-like strings may also be passed

    >>> period_array(['2000-Q1', '2000-Q2', '2000-Q3', '2000-Q4'], freq='Q')
    <PeriodArray>
    ['2000Q1', '2000Q2', '2000Q3', '2000Q4']
    Length: 4, dtype: period[Q-DEC]
    """
data_dtype = getattr(data, "dtype", None)

if is_datetime64_dtype(data_dtype):
    exit(PeriodArray._from_datetime64(data, freq))
if is_period_dtype(data_dtype):
    exit(PeriodArray(data, freq=freq))

# other iterable of some kind
if not isinstance(data, (np.ndarray, list, tuple, ABCSeries)):
    data = list(data)

arrdata = np.asarray(data)

dtype: PeriodDtype | None
if freq:
    dtype = PeriodDtype(freq)
else:
    dtype = None

if is_float_dtype(arrdata) and len(arrdata) > 0:
    raise TypeError("PeriodIndex does not allow floating point in construction")

if is_integer_dtype(arrdata.dtype):
    arr = arrdata.astype(np.int64, copy=False)
    # error: Argument 2 to "from_ordinals" has incompatible type "Union[str,
    # Tick, None]"; expected "Union[timedelta, BaseOffset, str]"
    ordinals = libperiod.from_ordinals(arr, freq)  # type: ignore[arg-type]
    exit(PeriodArray(ordinals, dtype=dtype))

data = ensure_object(arrdata)

exit(PeriodArray._from_sequence(data, dtype=dtype))
