# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# For numeric data with NA and Inf (GH #13595)
s = Series([0, -np.inf, np.inf, np.nan])

assert s.idxmin() == 1
assert np.isnan(s.idxmin(skipna=False))

assert s.idxmax() == 2
assert np.isnan(s.idxmax(skipna=False))

# Using old-style behavior that treats floating point nan, -inf, and
# +inf as missing
with pd.option_context("mode.use_inf_as_na", True):
    assert s.idxmin() == 0
    assert np.isnan(s.idxmin(skipna=False))
    assert s.idxmax() == 0
    np.isnan(s.idxmax(skipna=False))
