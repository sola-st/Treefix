# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH#1646
rng = date_range("1/1/2000", "1/20/2000", freq="D")
ts = Series(np.random.randn(len(rng)), index=rng)

ts[::2] = np.nan

result = ts.interpolate(method="values")
exp = ts.interpolate()
tm.assert_series_equal(result, exp)
