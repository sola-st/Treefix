# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH 17717
p1 = Period("2017-09-01")
p2 = Period("2017-09-04")
p3 = Period("2017-09-07")

tp0 = Period("2017-08-31")
tp1 = Period("2017-09-02")
tp2 = Period("2017-09-05")
tp3 = Period("2017-09-09")

idx = PeriodIndex([p1, p2, p3])

tm.assert_numpy_array_equal(
    idx.get_indexer(idx), np.array([0, 1, 2], dtype=np.intp)
)

target = PeriodIndex([tp0, tp1, tp2, tp3])
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "pad"), np.array([-1, 0, 1, 2], dtype=np.intp)
)
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "backfill"), np.array([0, 1, 2, -1], dtype=np.intp)
)
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "nearest"), np.array([0, 0, 1, 2], dtype=np.intp)
)

res = idx.get_indexer(target, "nearest", tolerance=Timedelta("1 day"))
tm.assert_numpy_array_equal(res, np.array([0, 0, 1, -1], dtype=np.intp))
