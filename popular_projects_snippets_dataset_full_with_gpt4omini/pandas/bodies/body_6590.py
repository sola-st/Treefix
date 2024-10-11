# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
res1 = idx1.union(idx2, sort=None)
tm.assert_index_equal(res1, expected_sorted, exact=True)

res1 = idx1.union(idx2, sort=False)
tm.assert_index_equal(res1, expected_notsorted, exact=True)

res2 = idx2.union(idx1, sort=None)
res3 = Index(idx1._values, name=idx1.name).union(idx2, sort=None)
tm.assert_index_equal(res2, expected_sorted, exact=True)
tm.assert_index_equal(res3, expected_sorted, exact="equiv")
