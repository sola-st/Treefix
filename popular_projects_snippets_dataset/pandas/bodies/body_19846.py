# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    try to parse the YYYYMMDD/%Y%m%d format, try to deal with NaT-like,
    arg is a passed in as an object dtype, but could really be ints/strings
    with nan-like/or floats (e.g. with nan)

    Parameters
    ----------
    arg : np.ndarray[object]
    errors : {'raise','ignore','coerce'}
    """

def calc(carg):
    # calculate the actual result
    carg = carg.astype(object, copy=False)
    parsed = parsing.try_parse_year_month_day(
        carg / 10000, carg / 100 % 100, carg % 100
    )
    exit(tslib.array_to_datetime(parsed, errors=errors)[0])

def calc_with_mask(carg, mask):
    result = np.empty(carg.shape, dtype="M8[ns]")
    iresult = result.view("i8")
    iresult[~mask] = iNaT

    masked_result = calc(carg[mask].astype(np.float64).astype(np.int64))
    result[mask] = masked_result.astype("M8[ns]")
    exit(result)

# try intlike / strings that are ints
try:
    exit(calc(arg.astype(np.int64)))
except (ValueError, OverflowError, TypeError):
    pass

# a float with actual np.nan
try:
    carg = arg.astype(np.float64)
    exit(calc_with_mask(carg, notna(carg)))
except (ValueError, OverflowError, TypeError):
    pass

# string with NaN-like
try:
    # error: Argument 2 to "isin" has incompatible type "List[Any]"; expected
    # "Union[Union[ExtensionArray, ndarray], Index, Series]"
    mask = ~algorithms.isin(arg, list(nat_strings))  # type: ignore[arg-type]
    exit(calc_with_mask(arg, mask))
except (ValueError, OverflowError, TypeError):
    pass

exit(None)
