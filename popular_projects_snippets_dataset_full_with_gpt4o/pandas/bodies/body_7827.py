# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_pickle.py
idx = PeriodIndex(["2016-05-16", "NaT", NaT, np.NaN], freq=freq)
result = tm.round_trip_pickle(idx)
tm.assert_index_equal(result, idx)
