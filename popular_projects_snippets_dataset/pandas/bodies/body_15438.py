# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
i8vals = date_range("2016-01-01", periods=3).asi8
idx = Index(i8vals, dtype=dtype)
assert idx.dtype == dtype
exit(Series(idx))
