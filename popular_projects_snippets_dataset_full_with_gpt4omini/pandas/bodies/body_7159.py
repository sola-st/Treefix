# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index_cls = self._index_cls
cls_name = index_cls.__name__

# invalid
msg = (
    rf"{cls_name}\(\.\.\.\) must be called with a collection of "
    r"some kind, 0\.0 was passed"
)
with pytest.raises(TypeError, match=msg):
    index_cls(0.0)

msg = f"data is not compatible with {index_cls.__name__}"
with pytest.raises(ValueError, match=msg):
    index_cls(["a", "b", 0.0])

with pytest.raises(ValueError, match=msg):
    index_cls([Timestamp("20130101")])
