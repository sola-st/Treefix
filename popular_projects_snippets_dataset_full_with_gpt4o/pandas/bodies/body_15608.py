# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
index = np.arange(10)
s = Series(np.random.randn(10), index=index)

result = s[:2].reindex(index, method="pad", limit=5)

expected = s[:2].reindex(index).fillna(method="pad")
expected[-3:] = np.nan
tm.assert_series_equal(result, expected)

result = s[-2:].reindex(index, method="backfill", limit=5)

expected = s[-2:].reindex(index).fillna(method="backfill")
expected[:3] = np.nan
tm.assert_series_equal(result, expected)
