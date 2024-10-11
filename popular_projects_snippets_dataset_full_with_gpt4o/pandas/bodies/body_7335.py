# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
tidx = TimedeltaIndex(["1 days 01:00:00", "NaT", "2 days 01:00:00"])

assert tidx.get_loc(NaT) == 1
assert tidx.get_loc(None) == 1
assert tidx.get_loc(float("nan")) == 1
assert tidx.get_loc(np.nan) == 1
