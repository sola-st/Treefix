# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
from scipy.stats import skew

string_series = tm.makeStringSeries().rename("series")

alt = lambda x: skew(x, bias=False)
self._check_stat_op("skew", alt, string_series)

# test corner cases, skew() returns NaN unless there's at least 3
# values
min_N = 3
for i in range(1, min_N + 1):
    s = Series(np.ones(i))
    df = DataFrame(np.ones((i, i)))
    if i < min_N:
        assert np.isnan(s.skew())
        assert np.isnan(df.skew()).all()
    else:
        assert 0 == s.skew()
        assert (df.skew() == 0).all()
