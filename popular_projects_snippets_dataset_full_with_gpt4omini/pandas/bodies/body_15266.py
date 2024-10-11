# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
ser = Series(range(10), index=list(range(0, 20, 2)))
with pytest.raises(KeyError, match=r"^1$"):
    indexer_sl(ser)[1]
