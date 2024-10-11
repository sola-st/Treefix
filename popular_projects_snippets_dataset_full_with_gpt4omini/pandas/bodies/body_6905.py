# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
idx = Index(["c", "a", "b"])
tm.assert_index_equal(idx.intersection(idx, sort=False), idx)
tm.assert_index_equal(idx.intersection(idx, sort=None), idx)
