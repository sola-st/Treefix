# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
idx = DatetimeIndex(
    ["1/1/2000", "1/2/2000", "1/2/2000", "1/3/2000", "1/4/2000"]
)

ts = Series(np.random.randn(len(idx)), index=idx)

result = ts["1/2/2000":]
expected = ts[1:]
tm.assert_series_equal(result, expected)

result = ts["1/2/2000":"1/3/2000"]
expected = ts[1:4]
tm.assert_series_equal(result, expected)
