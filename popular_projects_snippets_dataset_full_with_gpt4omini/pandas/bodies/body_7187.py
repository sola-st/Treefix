# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index_cls = self._index_cls
dtype = np.float16

msg = "float16 indexes are not supported"

# explicit construction
with pytest.raises(NotImplementedError, match=msg):
    index_cls([1, 2, 3, 4, 5], dtype=dtype)

with pytest.raises(NotImplementedError, match=msg):
    index_cls(np.array([1, 2, 3, 4, 5]), dtype=dtype)

with pytest.raises(NotImplementedError, match=msg):
    index_cls([1.0, 2, 3, 4, 5], dtype=dtype)

with pytest.raises(NotImplementedError, match=msg):
    index_cls(np.array([1.0, 2, 3, 4, 5]), dtype=dtype)

with pytest.raises(NotImplementedError, match=msg):
    index_cls([1.0, 2, 3, 4, 5], dtype=dtype)

with pytest.raises(NotImplementedError, match=msg):
    index_cls(np.array([1.0, 2, 3, 4, 5]), dtype=dtype)

# nan handling
with pytest.raises(NotImplementedError, match=msg):
    index_cls([np.nan, np.nan], dtype=dtype)

with pytest.raises(NotImplementedError, match=msg):
    index_cls(np.array([np.nan]), dtype=dtype)
