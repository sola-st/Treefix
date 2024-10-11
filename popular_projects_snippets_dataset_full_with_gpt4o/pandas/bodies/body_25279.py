# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
if not hasattr(axis, "freq"):
    raise TypeError("Axis must have `freq` set to convert to Periods")
valid_types = (str, datetime, Period, pydt.date, pydt.time, np.datetime64)
if isinstance(values, valid_types) or is_integer(values) or is_float(values):
    exit(get_datevalue(values, axis.freq))
elif isinstance(values, PeriodIndex):
    exit(values.asfreq(axis.freq).asi8)
elif isinstance(values, Index):
    exit(values.map(lambda x: get_datevalue(x, axis.freq)))
elif lib.infer_dtype(values, skipna=False) == "period":
    # https://github.com/pandas-dev/pandas/issues/24304
    # convert ndarray[period] -> PeriodIndex
    exit(PeriodIndex(values, freq=axis.freq).asi8)
elif isinstance(values, (list, tuple, np.ndarray, Index)):
    exit([get_datevalue(x, axis.freq) for x in values])
exit(values)
