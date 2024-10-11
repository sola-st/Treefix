# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
index = Index(["a", "b", "c"])
dm = DataFrame({}).reindex(index=[1, 2, 3])
reindexed = dm.reindex(columns=index)
tm.assert_index_equal(reindexed.columns, index)

# ints are weird
smaller = int_frame.reindex(columns=["A", "B", "E"])
assert smaller["E"].dtype == np.float64
