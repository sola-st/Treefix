# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
msg = f"data is not compatible with {self._index_cls.__name__}"

# can't
data = ["foo", "bar", "baz"]
with pytest.raises(ValueError, match=msg):
    self._index_cls(data)

# shouldn't
data = ["0", "1", "2"]
with pytest.raises(ValueError, match=msg):
    self._index_cls(data)
