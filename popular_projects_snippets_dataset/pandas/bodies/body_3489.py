# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
df = DataFrame(columns=["a", "b"], dtype="int64")

res = df.quantile(0.5, interpolation=interpolation, method=method)
exp = Series([np.nan, np.nan], index=["a", "b"], name=0.5)
tm.assert_series_equal(res, exp)
