# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
# GH#40397
obj = tm.round_trip_pickle(lib.no_default)
assert obj is lib.no_default
