# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# IntervalIndex needs non-overlapping for uniqueness when querying
index = IntervalIndex.from_tuples(tuples, closed=closed)

msg = (
    "cannot handle overlapping indices; use "
    "IntervalIndex.get_indexer_non_unique"
)
with pytest.raises(InvalidIndexError, match=msg):
    index.get_indexer([0, 2])
