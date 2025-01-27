# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
rng = pd.period_range("1/1/2000", "1/1/2010", freq="A")
ts = Series(np.random.randn(len(rng)), index=rng)

result = ts + ts[::2]
expected = ts + ts
expected.iloc[1::2] = np.nan
tm.assert_series_equal(result, expected)

result = ts + _permute(ts[::2])
tm.assert_series_equal(result, expected)

msg = "Input has different freq=D from Period\\(freq=A-DEC\\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    ts + ts.asfreq("D", how="end")
