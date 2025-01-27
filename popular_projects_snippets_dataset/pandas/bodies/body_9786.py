# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 8238
vals = np.array(range(10), dtype=float)
xp = vals.copy()
xp[:2] = np.nan
xp[-2:] = np.nan
xp = Series(xp)[::step]

rs = Series(vals).rolling(5, win_type=win_types, center=True, step=step).mean()
tm.assert_series_equal(xp, rs)
