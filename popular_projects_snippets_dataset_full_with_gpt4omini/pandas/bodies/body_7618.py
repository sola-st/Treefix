# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
i = MultiIndex.from_tuples([("A", 1), ("A", 2)])

msg = r"\.where is not supported for MultiIndex operations"
with pytest.raises(NotImplementedError, match=msg):
    i.where(True)
