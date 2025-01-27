# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
rng = date_range("1/1/2000", periods=20)
ts = Series(np.random.randn(20), index=rng)

result = ts.reindex(list(ts.index[5:10]))
expected = ts[5:10]
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)

result = ts[list(ts.index[5:10])]
tm.assert_series_equal(result, expected)
