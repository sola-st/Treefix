# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
rng = date_range("1/1/2000 0:00:00", periods=10000, freq="T").as_unit(unit)
ts = Series(np.random.randn(len(rng)), index=rng)
ts[:2] = np.nan  # so results are the same

result = ts[2:].resample("D", closed="left", label="left").mean()
expected = ts.resample("D", closed="left", label="left").mean()
tm.assert_series_equal(result, expected)
