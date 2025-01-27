# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
index_cls = self._index_cls

idx = index_cls([], dtype=dtype, name="Foo")
idx_view = idx.view()
assert idx_view.name == "Foo"

idx_view = idx.view(dtype)
tm.assert_index_equal(idx, index_cls(idx_view, name="Foo"), exact=True)

idx_view = idx.view(index_cls)
tm.assert_index_equal(idx, index_cls(idx_view, name="Foo"), exact=True)
