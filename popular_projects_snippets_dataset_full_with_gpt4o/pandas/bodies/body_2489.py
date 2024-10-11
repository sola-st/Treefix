# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
rng = period_range("1/1/2000", periods=5)
df = DataFrame(np.random.randn(10, 5), columns=rng)

ts = df[rng[0]]
tm.assert_series_equal(ts, df.iloc[:, 0])

# GH#1211; smoketest unrelated to the rest of this test
repr(df)

ts = df["1/1/2000"]
tm.assert_series_equal(ts, df.iloc[:, 0])
