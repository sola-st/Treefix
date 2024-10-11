# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
idx = to_timedelta(["0 days", "1 days", "2 days"])
tm.assert_numpy_array_equal(
    idx.get_indexer(idx), np.array([0, 1, 2], dtype=np.intp)
)

target = to_timedelta(["-1 hour", "12 hours", "1 day 1 hour"])
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "pad"), np.array([-1, 0, 1], dtype=np.intp)
)
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "backfill"), np.array([0, 1, 2], dtype=np.intp)
)
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "nearest"), np.array([0, 1, 1], dtype=np.intp)
)

res = idx.get_indexer(target, "nearest", tolerance=Timedelta("1 hour"))
tm.assert_numpy_array_equal(res, np.array([0, -1, 1], dtype=np.intp))
