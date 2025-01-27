# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Analogue to get_indexer that raises if any elements are missing.
        """
keyarr = key
if not isinstance(keyarr, Index):
    keyarr = com.asarray_tuplesafe(keyarr)

if self._index_as_unique:
    indexer = self.get_indexer_for(keyarr)
    keyarr = self.reindex(keyarr)[0]
else:
    keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)

self._raise_if_missing(keyarr, indexer, axis_name)

keyarr = self.take(indexer)
if isinstance(key, Index):
    # GH 42790 - Preserve name from an Index
    keyarr.name = key.name
if keyarr.dtype.kind in ["m", "M"]:
    # DTI/TDI.take can infer a freq in some cases when we dont want one
    if isinstance(key, list) or (
        isinstance(key, type(self))
        # "Index" has no attribute "freq"
        and key.freq is None  # type: ignore[attr-defined]
    ):
        keyarr = keyarr._with_freq(None)

exit((keyarr, indexer))
