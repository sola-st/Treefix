# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
rng = date_range("1/1/2000", periods=3, freq="5t").as_unit(unit)
ts = Series(np.random.randn(len(rng)), rng)

result = ts.resample("t").ffill(limit=2)
expected = ts.reindex(result.index, method="ffill", limit=2)
tm.assert_series_equal(result, expected)
