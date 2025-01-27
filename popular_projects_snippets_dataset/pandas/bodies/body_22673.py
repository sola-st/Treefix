# Extracted from ./data/repos/pandas/pandas/core/series.py
key = com.asarray_tuplesafe(key)
indexer: np.ndarray = self.index.get_indexer(key)
mask = indexer == -1
if mask.any():
    raise KeyError(f"{key[mask]} not in index")
self._set_values(indexer, value)
