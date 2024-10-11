# Extracted from ./data/repos/pandas/pandas/tests/series/test_missing.py
s = Series(["a", np.inf, np.nan, pd.NA, 1.0])
with pd.option_context("mode.use_inf_as_na", True):
    r = s.isna()
    dr = s.dropna()
e = Series([False, True, True, True, False])
de = Series(["a", 1.0], index=[0, 4])
tm.assert_series_equal(r, e)
tm.assert_series_equal(dr, de)
