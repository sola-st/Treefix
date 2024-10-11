# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_take.py
indices = [1, 2]

msg = r"take\(\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg):
    idx.take(indices, foo=2)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    idx.take(indices, out=indices)

msg = "the 'mode' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    idx.take(indices, mode="clip")
