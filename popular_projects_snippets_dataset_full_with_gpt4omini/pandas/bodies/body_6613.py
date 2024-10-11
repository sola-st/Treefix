# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
result = self._index_cls(1, 3)
expected = np.array([1, 2], dtype=dtype)
tm.assert_numpy_array_equal(result._data, expected)
