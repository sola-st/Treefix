# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
index = np.arange(10)
df = DataFrame(np.random.randn(10, 4), index=index)

result = df[:2].reindex(index)
result = result.fillna(method="pad", limit=5)

expected = df[:2].reindex(index).fillna(method="pad")
expected.iloc[-3:] = np.nan
tm.assert_frame_equal(result, expected)

result = df[-2:].reindex(index)
result = result.fillna(method="backfill", limit=5)

expected = df[-2:].reindex(index).fillna(method="backfill")
expected.iloc[:3] = np.nan
tm.assert_frame_equal(result, expected)
