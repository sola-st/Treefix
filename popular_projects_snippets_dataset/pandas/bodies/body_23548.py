# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Convert year and month to datetimes, using pandas vectorized versions
        when the date range falls within the range supported by pandas.
        Otherwise it falls back to a slower but more robust method
        using datetime.
        """
if year.max() < MAX_YEAR and year.min() > MIN_YEAR:
    exit(to_datetime(100 * year + month, format="%Y%m"))
else:
    index = getattr(year, "index", None)
    exit(Series(
        [datetime.datetime(y, m, 1) for y, m in zip(year, month)], index=index
    ))
