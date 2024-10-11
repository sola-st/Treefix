# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#42825 enforced in 2.0
df = DataFrame(
    [[1, 2], [3, 4]],
    columns=["a", "b"],
    index=MultiIndex.from_tuples([(1, 2), (3, 4)]),
)
with pytest.raises(TypeError, match="as an indexer is not supported"):
    df.loc[key] = 1
