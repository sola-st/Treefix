# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
ts = Series(np.random.randn(len(rng)), index=rng)

mask = (rng.hour == 9) & (rng.minute == 30)
result = ts[time(9, 30)]
expected = ts[mask]
result.index = result.index._with_freq(None)
tm.assert_series_equal(result, expected)
