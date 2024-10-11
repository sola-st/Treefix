# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py

q = datetime_series.quantile(0.1)
assert q == np.percentile(datetime_series.dropna(), 10)

q = datetime_series.quantile(0.9)
assert q == np.percentile(datetime_series.dropna(), 90)

# object dtype
q = Series(datetime_series, dtype=object).quantile(0.9)
assert q == np.percentile(datetime_series.dropna(), 90)

# datetime64[ns] dtype
dts = datetime_series.index.to_series()
q = dts.quantile(0.2)
assert q == Timestamp("2000-01-10 19:12:00")

# timedelta64[ns] dtype
tds = dts.diff()
q = tds.quantile(0.25)
assert q == pd.to_timedelta("24:00:00")

# GH7661
result = Series([np.timedelta64("NaT")]).sum()
assert result == pd.Timedelta(0)

msg = "percentiles should all be in the interval \\[0, 1\\]"
for invalid in [-1, 2, [0.5, -1], [0.5, 2]]:
    with pytest.raises(ValueError, match=msg):
        datetime_series.quantile(invalid)
