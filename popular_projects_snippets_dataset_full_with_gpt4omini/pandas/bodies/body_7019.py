# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
idx = CategoricalIndex([1, 2, 3], name="foo")
indices = [1, 0, -1]

msg = r"take\(\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg):
    idx.take(indices, foo=2)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    idx.take(indices, out=indices)

msg = "the 'mode' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    idx.take(indices, mode="clip")
