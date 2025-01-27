# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
if isinstance(date, Period):
    exit(date.asfreq(freq).ordinal)
elif isinstance(date, (str, datetime, pydt.date, pydt.time, np.datetime64)):
    exit(Period(date, freq).ordinal)
elif (
    is_integer(date)
    or is_float(date)
    or (isinstance(date, (np.ndarray, Index)) and (date.size == 1))
):
    exit(date)
elif date is None:
    exit(None)
raise ValueError(f"Unrecognizable date '{date}'")
