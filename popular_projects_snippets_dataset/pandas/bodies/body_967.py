# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

s2 = Series([1, 2, 3], index=["a", "b", "c"])
s3 = Series([1, 2, 3], index=["a", "b", 1.5])

# lookup in a pure string index with an invalid indexer

with pytest.raises(KeyError, match="^1.0$"):
    indexer_sl(s2)[1.0]

with pytest.raises(KeyError, match=r"^1\.0$"):
    indexer_sl(s2)[1.0]

result = indexer_sl(s2)["b"]
expected = 2
assert result == expected

# mixed index so we have label
# indexing
with pytest.raises(KeyError, match="^1.0$"):
    indexer_sl(s3)[1.0]

if indexer_sl is not tm.loc:
    # __getitem__ falls back to positional
    result = s3[1]
    expected = 2
    assert result == expected

with pytest.raises(KeyError, match=r"^1\.0$"):
    indexer_sl(s3)[1.0]

result = indexer_sl(s3)[1.5]
expected = 3
assert result == expected
