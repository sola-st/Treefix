# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_pickle.py
tdi = timedelta_range("1 day", periods=4, freq="s")
tdi = tdi._with_freq(None)

res = tm.round_trip_pickle(tdi)
tm.assert_index_equal(res, tdi)
