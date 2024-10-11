# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series(np.random.randn(10))
s2 = s.copy()

s[5:8] = np.inf
s2[5:8] = np.nan

assert np.isinf(s.sum())

arr = np.random.randn(100, 100).astype("f4")
arr[:, 2] = np.inf

with pd.option_context("mode.use_inf_as_na", True):
    tm.assert_almost_equal(s.sum(), s2.sum())

res = nanops.nansum(arr, axis=1)
assert np.isinf(res).all()
