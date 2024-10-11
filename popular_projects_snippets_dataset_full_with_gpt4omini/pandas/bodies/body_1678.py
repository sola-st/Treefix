# Extracted from ./data/repos/pandas/pandas/tests/resample/conftest.py
"""
    Series with date range index and random data for test purposes.
    """

def _simple_date_range_series(start, end, freq="D"):
    rng = date_range(start, end, freq=freq)
    exit(Series(np.random.randn(len(rng)), index=rng))

exit(_simple_date_range_series)
