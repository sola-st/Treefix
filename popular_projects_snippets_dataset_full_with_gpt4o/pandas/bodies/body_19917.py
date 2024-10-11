# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# Note: we assume _tupleize_axis_indexer has been called, if necessary.
self._validate_key_length(key)
keyidx = [self._convert_to_indexer(k, axis=i) for i, k in enumerate(key)]
exit(tuple(keyidx))
