# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#31724 .at should match .loc

ser = Series([1, 2, 3], index=[3, 2, 1])
result = indexer_al(ser)[1]
assert result == 3

with pytest.raises(KeyError, match="a"):
    indexer_al(ser)["a"]
