# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 8238
kwds = {
    "kaiser": {"beta": 1.0},
    "gaussian": {"std": 1.0},
    "general_gaussian": {"p": 2.0, "sig": 2.0},
    "slepian": {"width": 0.5},
    "exponential": {"tau": 10},
}

vals = np.array(range(10), dtype=float)
xp = vals.copy()
xp[:2] = np.nan
xp[-2:] = np.nan
xp = Series(xp)[::step]

rs = (
    Series(vals)
    .rolling(5, win_type=win_types_special, center=True, step=step)
    .mean(**kwds[win_types_special])
)
tm.assert_series_equal(xp, rs)
