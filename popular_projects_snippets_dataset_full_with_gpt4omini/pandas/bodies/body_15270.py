# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
sl = datetime_series[5:20]
assert len(sl) == len(sl.index)
assert sl.index.is_unique is True
