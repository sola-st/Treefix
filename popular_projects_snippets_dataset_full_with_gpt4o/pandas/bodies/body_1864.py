# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
rng = date_range(start, end, freq=freq)
ts = Series(data, index=rng)

res = ts.resample(resample_freq, origin=origin, closed=closed).sum()
expected = Series(
    exp_data,
    index=date_range(end=exp_end, freq=resample_freq, periods=exp_periods),
)

tm.assert_series_equal(res, expected)
