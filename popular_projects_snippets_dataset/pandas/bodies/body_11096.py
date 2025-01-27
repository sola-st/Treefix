# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
df = tm.makeTimeDataFrame()
grouped = df.groupby([lambda x: x.year, lambda x: x.month, lambda x: x.day])
agged = grouped.sum()
tm.assert_almost_equal(df.values, agged.values)

grouped = df.T.groupby(
    [lambda x: x.year, lambda x: x.month, lambda x: x.day], axis=1
)

agged = grouped.agg(lambda x: x.sum())
tm.assert_index_equal(agged.index, df.columns)
tm.assert_almost_equal(df.T.values, agged.values)

agged = grouped.agg(lambda x: x.sum())
tm.assert_almost_equal(df.T.values, agged.values)
