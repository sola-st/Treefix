# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_pickle.py
rng = date_range("2009-01-01", "2010-01-01", freq=freq)
unpickled = tm.round_trip_pickle(rng)
assert unpickled.freq == freq
