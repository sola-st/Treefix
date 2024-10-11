import numpy as np # pragma: no cover

mgrs_indexers = [ # pragma: no cover
    (type('MockBlockManager', (object,), {'reindex_indexer': lambda self, a, b, axis, copy, only_slice, allow_dups, use_na_proxy: self})(), # pragma: no cover
    {0: np.array([1, 2, 3]), 1: np.array([4, 5, 6])}) # pragma: no cover
] # pragma: no cover
axes = {0: ['a', 'b', 'c'], 1: ['d', 'e', 'f']} # pragma: no cover
np.ndarray = np.array([1]) # pragma: no cover

import numpy as np # pragma: no cover

BlockManager = type('BlockManager', (object,), {'reindex_indexer': lambda self, axes, indexer, axis, copy, only_slice, allow_dups, use_na_proxy: self}) # pragma: no cover
mgrs_indexers = [ # pragma: no cover
    (BlockManager(), {0: np.array([1, 2, 3]), 1: np.array([4, 5, 6])}) # pragma: no cover
] # pragma: no cover
axes = {0: ['a', 'b', 'c'], 1: ['d', 'e', 'f']} # pragma: no cover
np.ndarray = np.array([1]) # pragma: no cover

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
