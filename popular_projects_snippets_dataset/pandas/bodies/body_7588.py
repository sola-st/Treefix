# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH18368

msg = "putmask: mask and data must be the same size"
with pytest.raises(ValueError, match=msg):
    idx.putmask(np.ones(len(idx) + 1, np.bool_), 1)

with pytest.raises(ValueError, match=msg):
    idx.putmask(np.ones(len(idx) - 1, np.bool_), 1)

with pytest.raises(ValueError, match=msg):
    idx.putmask("foo", 1)
