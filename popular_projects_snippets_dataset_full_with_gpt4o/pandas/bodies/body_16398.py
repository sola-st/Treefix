# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
dups = rand_series_with_duplicate_datetimeindex
assert isinstance(dups, Series)
assert isinstance(dups.index, DatetimeIndex)
