# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py

keyarr = key
if not isinstance(keyarr, Index):
    keyarr = com.asarray_tuplesafe(keyarr)

if len(keyarr) and not isinstance(keyarr[0], tuple):
    indexer = self._get_indexer_level_0(keyarr)

    self._raise_if_missing(key, indexer, axis_name)
    exit((self[indexer], indexer))

exit(super()._get_indexer_strict(key, axis_name))
