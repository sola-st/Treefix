# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
import scipy.stats  # noqa:F401
from scipy.stats import rankdata

float_frame.loc[::2, "A"] = np.nan
float_frame.loc[::3, "B"] = np.nan
float_frame.loc[::4, "C"] = np.nan
float_frame.loc[::5, "D"] = np.nan

ranks0 = float_frame.rank()
ranks1 = float_frame.rank(1)
mask = np.isnan(float_frame.values)

fvals = float_frame.fillna(np.inf).values

exp0 = np.apply_along_axis(rankdata, 0, fvals)
exp0[mask] = np.nan

exp1 = np.apply_along_axis(rankdata, 1, fvals)
exp1[mask] = np.nan

tm.assert_almost_equal(ranks0.values, exp0)
tm.assert_almost_equal(ranks1.values, exp1)

# integers
df = DataFrame(np.random.randint(0, 5, size=40).reshape((10, 4)))

result = df.rank()
exp = df.astype(float).rank()
tm.assert_frame_equal(result, exp)

result = df.rank(1)
exp = df.astype(float).rank(1)
tm.assert_frame_equal(result, exp)
