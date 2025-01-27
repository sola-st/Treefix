# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
import scipy.stats  # noqa:F401
from scipy.stats import rankdata

float_frame.loc[::2, "A"] = np.nan
float_frame.loc[::3, "B"] = np.nan
float_frame.loc[::4, "C"] = np.nan
float_frame.loc[::5, "D"] = np.nan

# bottom
ranks0 = float_frame.rank(na_option="bottom")
ranks1 = float_frame.rank(1, na_option="bottom")

fvals = float_frame.fillna(np.inf).values

exp0 = np.apply_along_axis(rankdata, 0, fvals)
exp1 = np.apply_along_axis(rankdata, 1, fvals)

tm.assert_almost_equal(ranks0.values, exp0)
tm.assert_almost_equal(ranks1.values, exp1)

# top
ranks0 = float_frame.rank(na_option="top")
ranks1 = float_frame.rank(1, na_option="top")

fval0 = float_frame.fillna((float_frame.min() - 1).to_dict()).values
fval1 = float_frame.T
fval1 = fval1.fillna((fval1.min() - 1).to_dict()).T
fval1 = fval1.fillna(np.inf).values

exp0 = np.apply_along_axis(rankdata, 0, fval0)
exp1 = np.apply_along_axis(rankdata, 1, fval1)

tm.assert_almost_equal(ranks0.values, exp0)
tm.assert_almost_equal(ranks1.values, exp1)

# descending

# bottom
ranks0 = float_frame.rank(na_option="top", ascending=False)
ranks1 = float_frame.rank(1, na_option="top", ascending=False)

fvals = float_frame.fillna(np.inf).values

exp0 = np.apply_along_axis(rankdata, 0, -fvals)
exp1 = np.apply_along_axis(rankdata, 1, -fvals)

tm.assert_almost_equal(ranks0.values, exp0)
tm.assert_almost_equal(ranks1.values, exp1)

# descending

# top
ranks0 = float_frame.rank(na_option="bottom", ascending=False)
ranks1 = float_frame.rank(1, na_option="bottom", ascending=False)

fval0 = float_frame.fillna((float_frame.min() - 1).to_dict()).values
fval1 = float_frame.T
fval1 = fval1.fillna((fval1.min() - 1).to_dict()).T
fval1 = fval1.fillna(np.inf).values

exp0 = np.apply_along_axis(rankdata, 0, -fval0)
exp1 = np.apply_along_axis(rankdata, 1, -fval1)

tm.assert_numpy_array_equal(ranks0.values, exp0)
tm.assert_numpy_array_equal(ranks1.values, exp1)

# bad values throw error
msg = "na_option must be one of 'keep', 'top', or 'bottom'"

with pytest.raises(ValueError, match=msg):
    float_frame.rank(na_option="bad", ascending=False)

# invalid type
with pytest.raises(ValueError, match=msg):
    float_frame.rank(na_option=True, ascending=False)
