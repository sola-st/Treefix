# Extracted from ./data/repos/pandas/pandas/tests/resample/conftest.py
"""
    Series with period range index and random data for test purposes.
    """

def _simple_period_range_series(start, end, freq="D"):
    rng = period_range(start, end, freq=freq)
    exit(Series(np.random.randn(len(rng)), index=rng))

exit(_simple_period_range_series)
