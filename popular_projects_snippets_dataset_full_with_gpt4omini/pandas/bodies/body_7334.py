# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
idx = to_timedelta(["0 days", "1 days", "2 days"])

# GH 16909
assert idx.get_loc(idx[1].to_timedelta64()) == 1

# GH 16896
assert idx.get_loc("0 days") == 0
