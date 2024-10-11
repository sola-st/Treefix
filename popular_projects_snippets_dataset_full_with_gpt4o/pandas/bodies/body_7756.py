# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# MultiIndex and Index raise TypeError, others InvalidIndexError

with pytest.raises((TypeError, InvalidIndexError), match="slice"):
    index.get_loc(slice(0, 1))
