# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
major_axis = Index(np.arange(4))
minor_axis = Index(np.arange(2))

major_codes = np.array([0, 0, 1, 2, 2, 3, 3], dtype=np.intp)
minor_codes = np.array([0, 1, 0, 0, 1, 0, 1], dtype=np.intp)

index = MultiIndex(
    levels=[major_axis, minor_axis], codes=[major_codes, minor_codes]
)
idx1 = index[:5]
idx2 = index[[1, 3, 5]]

r1 = idx1.get_indexer(idx2)
tm.assert_almost_equal(r1, np.array([1, 3, -1], dtype=np.intp))

r1 = idx2.get_indexer(idx1, method="pad")
e1 = np.array([-1, 0, 0, 1, 1], dtype=np.intp)
tm.assert_almost_equal(r1, e1)

r2 = idx2.get_indexer(idx1[::-1], method="pad")
tm.assert_almost_equal(r2, e1[::-1])

rffill1 = idx2.get_indexer(idx1, method="ffill")
tm.assert_almost_equal(r1, rffill1)

r1 = idx2.get_indexer(idx1, method="backfill")
e1 = np.array([0, 0, 1, 1, 2], dtype=np.intp)
tm.assert_almost_equal(r1, e1)

r2 = idx2.get_indexer(idx1[::-1], method="backfill")
tm.assert_almost_equal(r2, e1[::-1])

rbfill1 = idx2.get_indexer(idx1, method="bfill")
tm.assert_almost_equal(r1, rbfill1)

# pass non-MultiIndex
r1 = idx1.get_indexer(idx2.values)
rexp1 = idx1.get_indexer(idx2)
tm.assert_almost_equal(r1, rexp1)

r1 = idx1.get_indexer([1, 2, 3])
assert (r1 == [-1, -1, -1]).all()

# create index with duplicates
idx1 = Index(list(range(10)) + list(range(10)))
idx2 = Index(list(range(20)))

msg = "Reindexing only valid with uniquely valued Index objects"
with pytest.raises(InvalidIndexError, match=msg):
    idx1.get_indexer(idx2)
