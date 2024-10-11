# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 5835
# dups on index and missing values
df = DataFrame(np.random.randn(5, 5), columns=["A", "B", "B", "B", "A"])

with pytest.raises(KeyError, match="not in index"):
    df.loc[:, ["A", "B", "C"]]
