# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
df = pd.DataFrame({"a": pd.date_range("20190101", periods=3, tz="UTC")})

listify = df.apply(lambda x: x.array, axis=1)
result = listify.explode()
tm.assert_series_equal(result, df["a"].rename())
