# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_where.py
idx = Index(range(3))
mask = np.array([True, False, True])
res = idx.where(mask, "2")
expected = Index([0, "2", 2])
tm.assert_index_equal(res, expected)
