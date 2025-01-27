# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_asof.py
# basic asof test
rng = date_range("1/1/2000", "1/2/2000", freq="4h")
s = Series(np.arange(len(rng)), index=rng)
r = s.resample("2h").mean()

result = r.asof(r.index)
expected = Series(
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6.0],
    index=date_range("1/1/2000", "1/2/2000", freq="2h"),
)
tm.assert_series_equal(result, expected)

r.iloc[3:5] = np.nan
result = r.asof(r.index)
expected = Series(
    [0, 0, 1, 1, 1, 1, 3, 3, 4, 4, 5, 5, 6.0],
    index=date_range("1/1/2000", "1/2/2000", freq="2h"),
)
tm.assert_series_equal(result, expected)

r.iloc[-3:] = np.nan
result = r.asof(r.index)
expected = Series(
    [0, 0, 1, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4.0],
    index=date_range("1/1/2000", "1/2/2000", freq="2h"),
)
tm.assert_series_equal(result, expected)
