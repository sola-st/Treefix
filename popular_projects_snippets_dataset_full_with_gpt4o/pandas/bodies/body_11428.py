# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
unp_series = tm.round_trip_pickle(string_series)
tm.assert_series_equal(unp_series, string_series)
