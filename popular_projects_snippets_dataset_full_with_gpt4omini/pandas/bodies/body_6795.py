# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 31117
idx = IntervalIndex.from_tuples([(1, 3), (2, 4), (3, 5), (7, 10), (3, 10)])

msg = str(key)
with pytest.raises(InvalidIndexError, match=msg):
    idx.get_loc(key)
