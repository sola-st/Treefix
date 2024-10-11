# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
df = tm.makeTimeDataFrame()
stacked = df.stack()
idx = stacked.index

slob = slice(*idx.slice_locs(df.index[5], df.index[15]))
sliced = stacked[slob]
expected = df[5:16].stack()
tm.assert_almost_equal(sliced.values, expected.values)

slob = slice(
    *idx.slice_locs(
        df.index[5] + timedelta(seconds=30),
        df.index[15] - timedelta(seconds=30),
    )
)
sliced = stacked[slob]
expected = df[6:15].stack()
tm.assert_almost_equal(sliced.values, expected.values)
