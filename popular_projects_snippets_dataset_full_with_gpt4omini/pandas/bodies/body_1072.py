# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# GH#11372
idx = MultiIndex.from_product(
    [["A", "B", "C"], date_range("2015-01-01", "2015-04-01", freq="MS")]
)
cols = MultiIndex.from_product(
    [["foo", "bar"], date_range("2016-01-01", "2016-02-01", freq="MS")]
)

df = DataFrame(np.random.random((12, 4)), index=idx, columns=cols)

subidx = MultiIndex.from_tuples(
    [("A", Timestamp("2015-01-01")), ("A", Timestamp("2015-02-01"))]
)
subcols = MultiIndex.from_tuples(
    [("foo", Timestamp("2016-01-01")), ("foo", Timestamp("2016-02-01"))]
)

vals = DataFrame(np.random.random((2, 2)), index=subidx, columns=subcols)
self.check(
    target=df,
    indexers=(subidx, subcols),
    value=vals,
    compare_fn=tm.assert_frame_equal,
)
# set all columns
vals = DataFrame(np.random.random((2, 4)), index=subidx, columns=cols)
self.check(
    target=df,
    indexers=(subidx, slice(None, None, None)),
    value=vals,
    compare_fn=tm.assert_frame_equal,
)
# identity
copy = df.copy()
self.check(
    target=df,
    indexers=(df.index, df.columns),
    value=df,
    compare_fn=tm.assert_frame_equal,
    expected=copy,
)
