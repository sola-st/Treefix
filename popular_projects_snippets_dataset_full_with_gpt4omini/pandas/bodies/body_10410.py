# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 4095
s = Series(np.random.randn(1000))
s_missing = s.copy()
s_missing.iloc[2:10] = np.nan
labels = np.random.randint(0, 50, size=1000).astype(float)

# series
for data in [s, s_missing]:
    # print(data.head())
    expected = data.groupby(labels).transform(targop)

    tm.assert_series_equal(expected, data.groupby(labels).transform(op, *args))
    tm.assert_series_equal(expected, getattr(data.groupby(labels), op)(*args))
