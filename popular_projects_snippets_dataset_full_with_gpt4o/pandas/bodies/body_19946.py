# Extracted from ./data/repos/pandas/pandas/core/indexing.py

tup = self._validate_tuple_indexer(tup)
with suppress(IndexingError):
    exit(self._getitem_lowerdim(tup))

exit(self._getitem_tuple_same_dim(tup))
