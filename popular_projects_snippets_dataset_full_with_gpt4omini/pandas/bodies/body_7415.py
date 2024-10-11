# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reindex.py
result, indexer = idx.reindex(list(idx[:4]))
assert isinstance(result, MultiIndex)
assert result.names == ["first", "second"]
assert [level.name for level in result.levels] == ["first", "second"]

result, indexer = idx.reindex(list(idx))
assert isinstance(result, MultiIndex)
assert indexer is None
assert result.names == ["first", "second"]
assert [level.name for level in result.levels] == ["first", "second"]
