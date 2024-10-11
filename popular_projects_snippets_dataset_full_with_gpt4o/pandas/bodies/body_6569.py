# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
# GH 35611
unpickled = tm.round_trip_pickle(obj)
assert type(obj) == type(unpickled)
