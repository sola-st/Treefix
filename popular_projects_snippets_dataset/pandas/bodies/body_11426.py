# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py

unpickled = tm.round_trip_pickle(tm.makeTimeSeries(name=name))
assert unpickled.name == name
