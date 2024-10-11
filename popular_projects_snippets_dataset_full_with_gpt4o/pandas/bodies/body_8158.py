# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_pickle.py
# GH#8367
# round-trip of timezone
index = date_range("20130101", periods=3, tz="US/Eastern", name="foo")
unpickled = tm.round_trip_pickle(index)
tm.assert_index_equal(index, unpickled)
