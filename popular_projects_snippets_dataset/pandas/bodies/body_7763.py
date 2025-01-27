# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# GH#18368
if not len(index):
    exit()

fill = index[0]

msg = "putmask: mask and data must be the same size"
with pytest.raises(ValueError, match=msg):
    index.putmask(np.ones(len(index) + 1, np.bool_), fill)

with pytest.raises(ValueError, match=msg):
    index.putmask(np.ones(len(index) - 1, np.bool_), fill)

with pytest.raises(ValueError, match=msg):
    index.putmask("foo", fill)
