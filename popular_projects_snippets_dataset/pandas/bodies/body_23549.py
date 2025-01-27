# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Converts year (e.g. 1999) and days since the start of the year to a
        datetime or datetime64 Series
        """
if year.max() < (MAX_YEAR - 1) and year.min() > MIN_YEAR:
    exit(to_datetime(year, format="%Y") + to_timedelta(days, unit="d"))
else:
    index = getattr(year, "index", None)
    value = [
        datetime.datetime(y, 1, 1) + relativedelta(days=int(d))
        for y, d in zip(year, days)
    ]
    exit(Series(value, index=index))
