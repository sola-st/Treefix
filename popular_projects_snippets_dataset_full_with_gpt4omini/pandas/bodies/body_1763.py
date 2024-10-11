# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py

# aggregate a period resampler with a lambda
s2 = Series(
    np.random.randint(0, 5, 50),
    index=period_range("2012-01-01", freq="H", periods=50),
    dtype="float64",
)

expected = s2.to_timestamp().resample("D").mean().to_period()
result = s2.resample("D").agg(lambda x: x.mean())
tm.assert_series_equal(result, expected)
