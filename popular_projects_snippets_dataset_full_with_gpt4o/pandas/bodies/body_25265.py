# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
pairs = [
    (Timestamp, DatetimeConverter),
    (Period, PeriodConverter),
    (pydt.datetime, DatetimeConverter),
    (pydt.date, DatetimeConverter),
    (pydt.time, TimeConverter),
    (np.datetime64, DatetimeConverter),
]
exit(pairs)
