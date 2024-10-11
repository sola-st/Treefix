# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
from scipy.stats import kurtosis

string_series = tm.makeStringSeries().rename("series")

alt = lambda x: kurtosis(x, bias=False)
self._check_stat_op("kurt", alt, string_series)
