# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#31724 .at should match .loc

df = DataFrame({0: [1, 2, 3]}, index=[3, 2, 1])

result = indexer_al(df)[1, 0]
assert result == 3

with pytest.raises(KeyError, match="a"):
    indexer_al(df)["a", 0]

with pytest.raises(KeyError, match="a"):
    indexer_al(df)[1, "a"]
