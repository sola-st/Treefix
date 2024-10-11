# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
# datetimes
df = DataFrame(columns=["a", "b"], dtype="datetime64[ns]")

res = df.quantile(
    0.5, numeric_only=False, interpolation=interpolation, method=method
)
exp = Series(
    [pd.NaT, pd.NaT], index=["a", "b"], dtype="datetime64[ns]", name=0.5
)
tm.assert_series_equal(res, exp)

# Mixed dt64/dt64tz
df["a"] = df["a"].dt.tz_localize("US/Central")
res = df.quantile(
    0.5, numeric_only=False, interpolation=interpolation, method=method
)
exp = exp.astype(object)
tm.assert_series_equal(res, exp)

# both dt64tz
df["b"] = df["b"].dt.tz_localize("US/Central")
res = df.quantile(
    0.5, numeric_only=False, interpolation=interpolation, method=method
)
exp = exp.astype(df["b"].dtype)
tm.assert_series_equal(res, exp)
