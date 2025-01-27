# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#31724 .at should match .loc
df = DataFrame({"A": [1, 2, 3]}, index=list("abc"))
result = indexer_al(df)["a", "A"]
assert result == 1

with pytest.raises(KeyError, match="^0$"):
    indexer_al(df)["a", 0]
