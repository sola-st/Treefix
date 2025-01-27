# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py
if dtype is dtlike_dtypes[-1]:
    # PeriodArray will try to cast ints to strings
    exit(DatetimeIndex(vals).astype(dtype))
exit(Index(vals, dtype=dtype))
