# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
idx = simple_index

idx_view = idx.view("i8")
result = self._index_cls(idx)
tm.assert_index_equal(result, idx)

idx_view = idx.view(self._index_cls)
result = self._index_cls(idx)
tm.assert_index_equal(result, idx_view)
