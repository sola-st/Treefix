# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_cov_corr.py
# full overlap
tm.assert_almost_equal(
    datetime_series.cov(datetime_series), datetime_series.std() ** 2
)

# partial overlap
tm.assert_almost_equal(
    datetime_series[:15].cov(datetime_series[5:]),
    datetime_series[5:15].std() ** 2,
)

# No overlap
assert np.isnan(datetime_series[::2].cov(datetime_series[1::2]))

# all NA
cp = datetime_series[:10].copy()
cp[:] = np.nan
assert isna(cp.cov(cp))

# min_periods
assert isna(datetime_series[:15].cov(datetime_series[5:], min_periods=12))

ts1 = datetime_series[:15].reindex(datetime_series.index)
ts2 = datetime_series[5:].reindex(datetime_series.index)
assert isna(ts1.cov(ts2, min_periods=12))
