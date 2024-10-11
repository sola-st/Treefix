# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# at should not fallback
# GH#7814
# GH#31724 .at should match .loc
ser = Series([1, 2, 3], index=list("abc"))
result = indexer_al(ser)["a"]
assert result == 1

with pytest.raises(KeyError, match="^0$"):
    indexer_al(ser)[0]
