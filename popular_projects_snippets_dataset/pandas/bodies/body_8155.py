# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_pickle.py
# GH#4606
idx = to_datetime(["2013-01-01", NaT, "2014-01-06"])
idx_p = tm.round_trip_pickle(idx)
assert idx_p[0] == idx[0]
assert idx_p[1] is NaT
assert idx_p[2] == idx[2]
