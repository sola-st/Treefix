# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#36490
df = DataFrame(
    np.ones((3, 4)), columns=pd.IntervalIndex.from_breaks(np.arange(5))
)

expected = df.iloc[:, 0]

res = df[0.5]
tm.assert_series_equal(res, expected)

res = df.loc[:, 0.5]
tm.assert_series_equal(res, expected)
