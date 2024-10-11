# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_indexing.py
index = Index(["b", "c"])

msg = r"unsupported operand type\(s\) for -: 'str' and 'str'"
with pytest.raises(TypeError, match=msg):
    index.get_indexer(["a", "b", "c", "d"], method="nearest")

with pytest.raises(TypeError, match=msg):
    index.get_indexer(["a", "b", "c", "d"], method="pad", tolerance=2)

with pytest.raises(TypeError, match=msg):
    index.get_indexer(
        ["a", "b", "c", "d"], method="pad", tolerance=[2, 2, 2, 2]
    )
