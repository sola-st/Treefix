# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
idx = date_range("2011-01-01", "2011-01-31", freq="D", name="idx")
indices = [1, 6, 5, 9, 10, 13, 15, 3]

msg = r"take\(\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg):
    idx.take(indices, foo=2)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    idx.take(indices, out=indices)

msg = "the 'mode' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    idx.take(indices, mode="clip")
