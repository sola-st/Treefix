# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_pickle.py
dti = date_range("20130101", periods=3, tz="US/Eastern", name="foo")
dti = dti._with_freq(None)

res = tm.round_trip_pickle(dti)
tm.assert_index_equal(res, dti)
