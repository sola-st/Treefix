# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
mi = MultiIndex.from_tuples([("A", 1), ("A", 2)])
cond = [False, True]
msg = r"\.where is not supported for MultiIndex operations"
with pytest.raises(NotImplementedError, match=msg):
    mi.where(listlike_box(cond))
