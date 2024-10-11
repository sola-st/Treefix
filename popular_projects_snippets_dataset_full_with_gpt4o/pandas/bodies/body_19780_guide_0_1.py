import numpy as np # pragma: no cover

class BlockManager: # pragma: no cover
    def __init__(self, axes): # pragma: no cover
        self.axes = axes # pragma: no cover
    def reindex_indexer(self, axes, indexers, axis, copy, only_slice, allow_dups, use_na_proxy): # pragma: no cover
        # Mock method for reindexing # pragma: no cover
        return self # pragma: no cover
axes = [0] # pragma: no cover
mgr1 = BlockManager(axes) # pragma: no cover
mgr2 = BlockManager(axes) # pragma: no cover
indexers1 = {0: np.array([0, 1])} # pragma: no cover
indexers2 = {0: np.array([1, 2])} # pragma: no cover
mgrs_indexers = [(mgr1, indexers1), (mgr2, indexers2)] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
from l3.Runtime import _l_
"""
    Reindex along columns so that all of the BlockManagers being concatenated
    have matching columns.

    Columns added in this reindexing have dtype=np.void, indicating they
    should be ignored when choosing a column's final dtype.
    """
new_mgrs_indexers: list[tuple[BlockManager, dict[int, np.ndarray]]] = []
_l_(22328)

for mgr, indexers in mgrs_indexers:
    _l_(22332)

    # For axis=0 (i.e. columns) we use_na_proxy and only_slice, so this
    #  is a cheap reindexing.
    for i, indexer in indexers.items():
        _l_(22330)

        mgr = mgr.reindex_indexer(
            axes[i],
            indexers[i],
            axis=i,
            copy=False,
            only_slice=True,  # only relevant for i==0
            allow_dups=True,
            use_na_proxy=True,  # only relevant for i==0
        )
        _l_(22329)
    new_mgrs_indexers.append((mgr, {}))
    _l_(22331)
aux = new_mgrs_indexers
_l_(22333)
exit(aux)
