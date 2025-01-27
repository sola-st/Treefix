# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
frame = DataFrame(
    np.ones((10, 2), dtype=bool), index=np.arange(0, 20, 2), columns=[0, 2]
)

reindexed = frame.reindex(np.arange(10))
assert reindexed.values.dtype == np.object_
assert isna(reindexed[0][1])

reindexed = frame.reindex(columns=range(3))
assert reindexed.values.dtype == np.object_
assert isna(reindexed[1]).all()
