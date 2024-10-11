# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH 4619; duplicate indexer with missing label
df = DataFrame({"A": vals})
with pytest.raises(KeyError, match="not in index"):
    df.loc[[0, 8, 0]]
