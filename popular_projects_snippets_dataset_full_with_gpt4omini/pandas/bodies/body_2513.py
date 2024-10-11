# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#42825 enforced in 2.0
df = DataFrame(
    [[1, 2], [3, 4]], columns=MultiIndex.from_tuples([("a", 1), ("b", 2)])
)
with pytest.raises(TypeError, match="as an indexer is not supported"):
    df[key]
