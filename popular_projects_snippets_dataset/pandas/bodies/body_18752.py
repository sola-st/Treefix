# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for Series with a DatetimeIndex that has duplicates.
    """
dates = [
    datetime(2000, 1, 2),
    datetime(2000, 1, 2),
    datetime(2000, 1, 2),
    datetime(2000, 1, 3),
    datetime(2000, 1, 3),
    datetime(2000, 1, 3),
    datetime(2000, 1, 4),
    datetime(2000, 1, 4),
    datetime(2000, 1, 4),
    datetime(2000, 1, 5),
]

exit(Series(np.random.randn(len(dates)), index=dates))
