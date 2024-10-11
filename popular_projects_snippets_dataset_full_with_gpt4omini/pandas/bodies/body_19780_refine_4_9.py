import numpy as np # pragma: no cover

axes = [np.array(['A', 'B', 'C']), np.array([0, 1, 2])] # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class MockBlockManager:  # Mocking BlockManager for testing purposes# pragma: no cover
    def __init__(self, data=None, axes=None):# pragma: no cover
        self.data = data if data is not None else np.empty((0, 0))# pragma: no cover
        self.axes = axes if axes is not None else []# pragma: no cover
    def reindex_indexer(self, axis, indexer, **kwargs):# pragma: no cover
        return self # pragma: no cover
mgrs_indexers = [(MockBlockManager(np.array([[1]]), ['A']), {0: np.array([0]), 1: np.array([1])})] # pragma: no cover
axes = [np.array(['A'])] # pragma: no cover

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
_l_(10837)

for mgr, indexers in mgrs_indexers:
    _l_(10841)

    # For axis=0 (i.e. columns) we use_na_proxy and only_slice, so this
    #  is a cheap reindexing.
    for i, indexer in indexers.items():
        _l_(10839)

        mgr = mgr.reindex_indexer(
            axes[i],
            indexers[i],
            axis=i,
            copy=False,
            only_slice=True,  # only relevant for i==0
            allow_dups=True,
            use_na_proxy=True,  # only relevant for i==0
        )
        _l_(10838)
    new_mgrs_indexers.append((mgr, {}))
    _l_(10840)
aux = new_mgrs_indexers
_l_(10842)
exit(aux)
