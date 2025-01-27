# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH 33939
rng = date_range("1/1/2000", periods=3, freq=freq, tz=tz_aware_fixture).as_unit(
    unit
)
ts = Series(np.random.randn(len(rng)), rng)

result = ts.resample(rule).nearest(limit=2)
expected = ts.reindex(result.index, method="nearest", limit=2)
tm.assert_series_equal(result, expected)
