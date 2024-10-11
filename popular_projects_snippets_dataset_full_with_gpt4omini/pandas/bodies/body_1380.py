# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#39004
df = DataFrame({"a": [1, 2, 3]})
indexer = DataFrame({"a": [True, False, True]})
msg = "DataFrame indexer for .iloc is not supported. Consider using .loc"
with pytest.raises(TypeError, match=msg):
    df.iloc[indexer] = 1

msg = (
    "DataFrame indexer is not allowed for .iloc\n"
    "Consider using .loc for automatic alignment."
)
with pytest.raises(IndexError, match=msg):
    df.iloc[indexer]
