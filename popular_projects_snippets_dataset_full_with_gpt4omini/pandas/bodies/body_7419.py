# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reindex.py
# GH7774
idx = MultiIndex.from_product([[0, 1], ["a", "b"]])
assert idx.reindex([], level=0)[0].levels[0].dtype.type == np.int64
assert idx.reindex([], level=1)[0].levels[1].dtype.type == np.object_

# case with EA levels
cat = pd.Categorical(["foo", "bar"])
dti = pd.date_range("2016-01-01", periods=2, tz="US/Pacific")
mi = MultiIndex.from_product([cat, dti])
assert mi.reindex([], level=0)[0].levels[0].dtype == cat.dtype
assert mi.reindex([], level=1)[0].levels[1].dtype == dti.dtype
