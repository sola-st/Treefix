import numpy as np # pragma: no cover
from pandas.core.internals import BlockManager # pragma: no cover

axes = [np.array(['a', 'b', 'c'])] # pragma: no cover

import numpy as np # pragma: no cover
from typing import List, Tuple, Dict # pragma: no cover

BlockManager = type('BlockManager', (object,), {'reindex_indexer': lambda self, *args, **kwargs: self}) # pragma: no cover
mgrs_indexers: List[Tuple[BlockManager, Dict[int, np.ndarray]]] = [(BlockManager(), {0: np.array([0, 1, 2]), 1: np.array([3, 4, 5])})] # pragma: no cover
axes = {0: np.array([0, 1, 2]), 1: np.array([3, 4, 5])} # pragma: no cover

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
