# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
idx = date_range("2000-01-01", periods=3)
key = idx[1].as_unit("ms")
loc = idx.get_loc(key)
assert loc == 1
assert key in idx
