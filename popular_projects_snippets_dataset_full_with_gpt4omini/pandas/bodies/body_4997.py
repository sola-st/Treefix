# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_stat_reductions.py
# test corner cases, kurt() returns NaN unless there's at least 4
# values
min_N = 4
for i in range(1, min_N + 1):
    s = Series(np.ones(i))
    df = DataFrame(np.ones((i, i)))
    if i < min_N:
        assert np.isnan(s.kurt())
        assert np.isnan(df.kurt()).all()
    else:
        assert 0 == s.kurt()
        assert (df.kurt() == 0).all()
