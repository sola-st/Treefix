# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_take.py
indexer = [4, 3, 0, 2]
result = idx.take(indexer)
expected = idx[indexer]
assert result.equals(expected)

# GH 10791
msg = "'MultiIndex' object has no attribute 'freq'"
with pytest.raises(AttributeError, match=msg):
    idx.freq
