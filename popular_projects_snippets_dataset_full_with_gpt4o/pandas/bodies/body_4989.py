# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
string_series = tm.makeStringSeries().rename("series")
self._check_stat_op("median", np.median, string_series)

# test with integers, test failure
int_ts = Series(np.ones(10, dtype=int), index=range(10))
tm.assert_almost_equal(np.median(int_ts), int_ts.median())
