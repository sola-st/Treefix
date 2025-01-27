# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
index_cls = self._index_cls

idx = Index([1, 2], dtype=dtype)
result = index_cls(idx)
expected = np.array([1, 2], dtype=idx.dtype)
tm.assert_numpy_array_equal(result._data, expected)
