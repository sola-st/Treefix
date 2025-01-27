# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_unique.py
index = rand_series_with_duplicate_datetimeindex.index
assert not index.is_unique
