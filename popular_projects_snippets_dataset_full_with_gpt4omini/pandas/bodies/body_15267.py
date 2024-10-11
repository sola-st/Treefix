# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# breaks reindex, so need to use .loc internally
# GH 4246
ser = Series([1, 2, 3, 4], ["foo", "bar", "foo", "bah"])
with pytest.raises(KeyError, match=re.escape("['bam'] not in index")):
    indexer_sl(ser)[["foo", "bar", "bah", "bam"]]
