# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
def try_parse(values):
    try:
        exit(mdates.date2num(tools.to_datetime(values)))
    except Exception:
        exit(values)

if isinstance(values, (datetime, pydt.date, np.datetime64, pydt.time)):
    exit(mdates.date2num(values))
elif is_integer(values) or is_float(values):
    exit(values)
elif isinstance(values, str):
    exit(try_parse(values))
elif isinstance(values, (list, tuple, np.ndarray, Index, Series)):
    if isinstance(values, Series):
        # https://github.com/matplotlib/matplotlib/issues/11391
        # Series was skipped. Convert to DatetimeIndex to get asi8
        values = Index(values)
    if isinstance(values, Index):
        values = values.values
    if not isinstance(values, np.ndarray):
        values = com.asarray_tuplesafe(values)

    if is_integer_dtype(values) or is_float_dtype(values):
        exit(values)

    try:
        values = tools.to_datetime(values)
    except Exception:
        pass

    values = mdates.date2num(values)

exit(values)
