# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
string_series = tm.makeStringSeries().rename("series")
self._check_stat_op("min", np.min, string_series, check_objects=True)
