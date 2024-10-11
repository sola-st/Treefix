# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
unp_ts = tm.round_trip_pickle(datetime_series)
tm.assert_series_equal(unp_ts, datetime_series)
