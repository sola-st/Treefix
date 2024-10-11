# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
original_name, index.name = index.name, "foo"
unpickled = tm.round_trip_pickle(index)
assert index.equals(unpickled)
index.name = original_name
