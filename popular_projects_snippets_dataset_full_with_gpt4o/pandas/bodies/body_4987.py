# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
string_series = tm.makeStringSeries().rename("series")
self._check_stat_op("sum", np.sum, string_series, check_allna=False)
