# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
rng = date_range("1/1/2011", periods=100, freq="H", tz="utc")

perm = np.random.permutation(100)[:90]
ser1 = Series(
    np.random.randn(90), index=rng.take(perm).tz_convert("US/Eastern")
)

perm = np.random.permutation(100)[:90]
ser2 = Series(
    np.random.randn(90), index=rng.take(perm).tz_convert("Europe/Berlin")
)

result = ser1 + ser2

uts1 = ser1.tz_convert("utc")
uts2 = ser2.tz_convert("utc")
expected = uts1 + uts2

assert result.index.tz is timezone.utc
tm.assert_series_equal(result, expected)
