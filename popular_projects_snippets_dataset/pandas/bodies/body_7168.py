# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index_cls = self._index_cls
# GH 11343
idx = Index([1.0, np.nan, 3.0], dtype=float, name="x")
# can't downcast
exp = Index([1.0, 0.1, 3.0], name="x")
tm.assert_index_equal(idx.fillna(0.1), exp, exact=True)

# downcast
exp = index_cls([1.0, 2.0, 3.0], name="x")
tm.assert_index_equal(idx.fillna(2), exp)

# object
exp = Index([1.0, "obj", 3.0], name="x")
tm.assert_index_equal(idx.fillna("obj"), exp, exact=True)
