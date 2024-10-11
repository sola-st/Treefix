# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
rng = date_range("1/1/2000", periods=20)
ts = Series(np.random.randn(20), index=rng)

ts_slice = ts[5:]
ts2 = ts_slice.copy()
ts2.index = [x.date() for x in ts2.index]

result = ts + ts2
result2 = ts2 + ts
expected = ts + ts[5:]
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)
tm.assert_series_equal(result2, expected)
