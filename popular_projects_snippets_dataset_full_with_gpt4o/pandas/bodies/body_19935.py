# Extracted from ./data/repos/pandas/pandas/core/indexing.py
with suppress(IndexingError):
    tup = self._expand_ellipsis(tup)
    exit(self._getitem_lowerdim(tup))

# no multi-index, so validate all of the indexers
tup = self._validate_tuple_indexer(tup)

# ugly hack for GH #836
if self._multi_take_opportunity(tup):
    exit(self._multi_take(tup))

exit(self._getitem_tuple_same_dim(tup))
