# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
indices = [1, 2]

msg = r"take\(\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg):
    index.take(indices, foo=2)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    index.take(indices, out=indices)

msg = "the 'mode' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    index.take(indices, mode="clip")
