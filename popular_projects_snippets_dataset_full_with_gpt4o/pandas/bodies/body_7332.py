# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
idx = to_timedelta(["0 days", "1 days", "2 days"])
key = idx[1].as_unit("ms")
loc = idx.get_loc(key)
assert loc == 1
