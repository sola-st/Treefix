# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py

N = 50
rng = period_range("1/1/1990", periods=N, freq="H")
ts = Series(np.random.randn(N), index=rng)

result = ts["1990-01-01 04"]
expected = ts[4]
assert result == expected

result = ts.copy()
result["1990-01-01 04"] = 0
result["1990-01-01 04"] = ts[4]
tm.assert_series_equal(result, ts)

result = ts["1990-01-01 04":"1990-01-01 07"]
expected = ts[4:8]
tm.assert_series_equal(result, expected)

result = ts.copy()
result["1990-01-01 04":"1990-01-01 07"] = 0
result["1990-01-01 04":"1990-01-01 07"] = ts[4:8]
tm.assert_series_equal(result, ts)

lb = "1990-01-01 04"
rb = "1990-01-01 07"
result = ts[(ts.index >= lb) & (ts.index <= rb)]
expected = ts[4:8]
tm.assert_series_equal(result, expected)

# GH 2782
result = ts[ts.index[4]]
expected = ts[4]
assert result == expected

result = ts[ts.index[4:8]]
expected = ts[4:8]
tm.assert_series_equal(result, expected)

result = ts.copy()
result[ts.index[4:8]] = 0
result.iloc[4:8] = ts.iloc[4:8]
tm.assert_series_equal(result, ts)
