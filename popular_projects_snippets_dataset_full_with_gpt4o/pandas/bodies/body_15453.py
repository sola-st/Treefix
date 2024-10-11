# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
data = [val] + list(obj[1:])
idx = IntervalIndex(data, dtype="Interval[float64]")
exit(Series(idx))
