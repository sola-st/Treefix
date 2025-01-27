# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH#38394
dtype = IntervalDtype("interval")

assert dtype._closed is None

tm.round_trip_pickle(dtype)
