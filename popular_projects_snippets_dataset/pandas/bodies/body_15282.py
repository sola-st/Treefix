# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH#46551
ser = Series([1])
indexer = Series([NA, False], dtype="boolean", index=[1, 2])
with pytest.raises(IndexingError, match="Unalignable"):
    ser.loc[indexer]
