# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH 17717
p1 = Period("2017-09-02")
p2 = Period("2017-09-03")
p3 = Period("2017-09-04")
p4 = Period("2017-09-05")

idx1 = PeriodIndex([p1, p2, p1])
idx2 = PeriodIndex([p2, p1, p3, p4])

result = idx1.get_indexer_non_unique(idx2)
expected_indexer = np.array([1, 0, 2, -1, -1], dtype=np.intp)
expected_missing = np.array([2, 3], dtype=np.intp)

tm.assert_numpy_array_equal(result[0], expected_indexer)
tm.assert_numpy_array_equal(result[1], expected_missing)
