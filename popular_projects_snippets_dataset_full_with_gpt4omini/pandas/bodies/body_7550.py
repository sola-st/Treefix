# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_partial_indexing.py
# Even though this syntax works on a single index, this is somewhat
# ambiguous and we don't want to extend this behavior forward to work
# in multi-indexes. This would amount to selecting a scalar from a
# column.
with pytest.raises(KeyError, match="'2016-01-01'"):
    df["2016-01-01"]
